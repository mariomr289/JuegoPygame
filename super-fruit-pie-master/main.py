#!/usr/bin/python
# -*- coding: utf-8 -*-

# Super Fruit Pie : basic 2D game
# made with pygame for Raspberry Pi
# David Art <david.madbox@gmail.com>

## Ressource ##

# Richard Jones <richard@mechanicalcat.net>
#    *** Intro to Game Programming tutorial ***
#    https://bitbucket.org/r1chardj0n3s/pygame-tutorial
#    http://pyvideo.org/video/1718/introduction-to-pygame

# Program Arcade Games With Python And Pygame - Build a Platformer
# http://programarcadegames.com

import pygame
import random
import sys
import time
import os

import gamelib.maps as maps
import gamelib.menu as menu
from gamelib.player import Player
from gamelib.enemy import Enemy


SETTINGS = {
    'music_volume': 50,
    'fx_volume': 90,
    'fullscreen': False,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'jump': pygame.K_SPACE
}

# because I use relative path ..
REALPATH = os.path.dirname( os.path.realpath( __file__ ) )
os.chdir(REALPATH)


class Platform (pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class Fruit(pygame.sprite.Sprite):

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/fruit/%s.png' % name)
        self.rect = self.image.get_rect()


class Mixer:

    def __init__(self, has_soundcard=False):
        self.has_soundcard = has_soundcard

        if has_soundcard:
            self.fx = {
                "jump": pygame.mixer.Sound("./sfx/jump.wav"),
                "crunch": pygame.mixer.Sound("./sfx/crunch.wav"),
                "flip": pygame.mixer.Sound("./sfx/flip.wav"),
                "no": pygame.mixer.Sound("./sfx/no.wav"),

            }

        #~ self.track = pygame.mixer.Sound("./sfx/track_1.wav")

    def play_fx(self, name):
        if self.has_soundcard:
            self.fx[name].set_volume(SETTINGS["fx_volume"]/100.0)
            self.fx[name].play()

    def play_track(self):
        if self.has_soundcard:
            self.track.set_volume(SETTINGS["music_volume"]/100.0)
            self.track.play()

    def set_music_volume(self, value):
        pass

    def set_sound_volume(self, value):
        pass


class Score:

    value = 0
    best = 0
    text = {}

    def __init__(self, game):
        self.game = game
        self.text = {
            "gameover": game.font.render("GAME OVER", 1, (255, 255, 255)),
            "gameover_shadow": game.font.render("GAME OVER", 1, (0, 0, 0)),
            "txt_score": game.font.render("SCORE", 1, (255, 255, 255)),
            "txt_score_shadow": game.font.render("SCORE", 1, (0, 0, 0)),
            "txt_best": game.font.render("BEST", 1, (255, 255, 255)),
            "txt_best_shadow": game.font.render("BEST", 1, (0, 0, 0)),
            "pause": game.font.render("PAUSE", 1, (255, 255, 255)),
            "pause_shadow": game.font.render("PAUSE", 1, (0, 0, 0)),
        }

        self.surf = pygame.Surface([game.width, game.height/2])
        self.surf.set_alpha(128)
        self.surf.fill((0, 0, 0))


    def update(self):
        self.value += 1
        if self.value > self.best:
            self.best = self.value
        self.render_score()

    def reset(self):
        self.value = 0
        self.render_score()

    def render(self):
        self.text["gameover"] = self.game.font.render("GAME OVER", 1, (255, 255, 255))
        self.text["gameover_shadow"] = self.game.font.render("GAME OVER", 1, (0, 0, 0))
        self.text["best"] = self.game.font.render(str(self.best), 1, (255, 255, 255))
        self.text["best_shadow"] = self.game.font.render(str(self.best), 1, (0, 0, 0))

    def render_score(self):
        self.text["score"] = self.game.font.render(str(self.value), 1, (255, 255, 255))
        self.text["score_shadow"] = self.game.font.render(str(self.value), 1, (0, 0, 0))

    def draw(self, screen):
        screen.blit(self.text["score_shadow"], (314, 4))
        screen.blit(self.text["score"], (310, 0))

    def draw_resume(self, screen):
        offset = self.game.height / 3
        screen.blit(self.surf, (0, offset))

        screen.blit(self.text["gameover_shadow"], (184, offset + 24))
        screen.blit(self.text["gameover"], (180, offset + 20))

        screen.blit(self.text["txt_score_shadow"], (184, offset + 84))
        screen.blit(self.text["txt_score"], (180, offset + 80))
        screen.blit(self.text["score_shadow"], (424, offset + 84))
        screen.blit(self.text["score"], (420, offset + 80))

        screen.blit(self.text["txt_best_shadow"], (184, offset + 144))
        screen.blit(self.text["txt_best"], (180, offset + 140))
        screen.blit(self.text["best_shadow"], (424, offset + 144))
        screen.blit(self.text["best"], (420, offset + 140))

    def draw_pause(self, screen):
        offset = self.game.height / 3
        screen.blit(self.surf, (0, offset))

        screen.blit(self.text["pause_shadow"], (244, offset + 84))
        screen.blit(self.text["pause"], (240, offset + 80))


class Game:

    width = 640
    height = 480
    map_ind = 0
    state = ""
    enemy_timer = 0
    enemy_next_timer = 0
    gameover_delay = 2000
    gameover_timer = 0

    def __init__(self):

        if SETTINGS["fullscreen"]:
            flags = pygame.FULLSCREEN
        else:
            flags = 0

        # pygame init
        pygame.init()
        try:
            pygame.mixer.init()
            self.has_soundcard = True
        except:
            self.has_soundcard = False
        pygame.mouse.set_visible(0)

        # init "buffer" and real screen
        self.screen = pygame.Surface([self.width, self.height])
        self.real_screen = pygame.display.set_mode([self.width, self.height], flags, 32)
        pygame.display.set_caption("Super Fruit Pie")

        # load game font
        self.font = pygame.font.Font("font/game_over.ttf", 120)

        # this is a bit more than score ..
        # I use it to show some info like pause, resume/gameover
        self.score = Score(self)

        # preload fruit image
        self.fruit = {
            "raspberry": Fruit("raspberry"),
            "orange": Fruit("orange"),
            "apple": Fruit("apple"),
            "banana": Fruit("banana"),
            "lemon": Fruit("lemon"),
            "cherry": Fruit("cherry"),
            "grape": Fruit("grape"),
        }

        # create mixer for fx/music
        self.mixer = Mixer(self.has_soundcard)

        # this is the main game menu
        self.menu = menu.Menu(self)

        # let's me introduce the player  :)
        self.player = Player(self)

        # maybe not the best way to manage menu/gameloop .. but here we go
        #~ self.mixer.play_track()
        self.menu.run()

    def init_game(self):
        # init game/player value for new game
        self.state = "play"
        self.player.rect.x, self.player.rect.y = self.player.start_pos
        self.fruit_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.add_fruit(1)
        self.add_enemy()
        self.score.reset()
        self.enemy_next_timer = 2 + random.random()*5

    def run(self):
        # main game loop ( need a complete rewrite .. really )
        self.load_map(self.map_ind)
        self.init_game()
        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)

            # tempo when gameover
            if self.state == "gameover":
                if self.gameover_timer < self.gameover_delay:
                    self.gameover_timer += dt
                    pygame.event.clear()
                else:
                    self.gameover_timer = 0
                    self.state = "waiting"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.state == "pause":
                            running = False
                        elif self.state == "play":
                            self.state = "pause"
                            self.draw()
                        elif self.state == "waiting":
                            self.state = "menu"
                            running = False
                    elif self.state == "waiting":
                        self.init_game()
                    elif self.state == "pause":
                        self.state = "play"

            if self.state == "play":
                # Enemy
                self.enemy_timer += dt / 1000.0
                if self.enemy_timer >= self.enemy_next_timer:
                    self.enemy_next_timer = 2 + random.random()*5
                    self.enemy_timer = 0
                    self.add_enemy()

                key = pygame.key.get_pressed()
                if key[SETTINGS["left"]]:
                    self.player.go_left()
                if key[SETTINGS["right"]]:
                    self.player.go_right()
                if key[SETTINGS["jump"]]:
                    self.player.jump()

                if self.player.is_dead:
                    self.state = "gameover"
                    self.score.render()
                    self.draw()
                    self.player.reset()

                elif running:
                    self.player.update(dt / 1000., self)
                    for enemy in self.enemy_list:
                        enemy.update(dt / 1000., self)
                        if enemy.is_dead:
                            self.enemy_list.remove(enemy)
                    self.draw()

    def draw(self):
        # background
        self.screen.blit(self.map_image, (0, 0))
        # score
        self.score.draw(self.screen)
        # player
        rect = self.player.anim_pos + (30, 30)
        pos = (self.player.rect.x, self.player.rect.y - 4)
        self.screen.blit(self.player.image, self.player.rect, rect)
        # fruit
        self.fruit_list.draw(self.screen)
        # enemy
        self.enemy_list.draw(self.screen)

        if self.state == "gameover":
            self.score.draw_resume(self.screen)
        elif self.state == "pause":
            self.score.draw_pause(self.screen)

        # and finally ..
        self.real_screen.blit(self.screen, (0, 0))
        pygame.display.flip()

    def load_map(self, map_ind):
        self.block_list = pygame.sprite.Group()
        mod = maps.model[self.map_ind]
        self.player.start_pos = mod["player"]

        for block in mod["platform"]:
            p = Platform(block[0], block[1], block[2], block[3])
            self.block_list.add(p)

        self.map_image = pygame.image.load('./images/%s' % mod["background"])

    def add_fruit(self, num):

        for ind in range(num):
            name = random.choice(list(self.fruit))
            fruit = self.fruit[name]
            fruit.rect.x = random.randint(2, 61) * 10
            fruit.rect.y = 100 + random.randint(0, 3) * 90
            self.fruit_list.add(fruit)

    def add_enemy(self):
        enemy = Enemy()
        self.enemy_list.add(enemy)


if __name__ == "__main__":

    game = Game()
    pygame.quit()
