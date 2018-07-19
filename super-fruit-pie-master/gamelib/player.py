import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load('./images/player.png')
        self.rect = pygame.Rect(0, 0, 30, 30)

        self.anim_state = {
            "idle": ((0, 0),),
            "jump_left": ((120, 30),(150,30)),
            "jump_right": ((120, 60),(150,60)),
            "walk_left": ((0,30),(30,30),(60,30),(90,30)),
            "walk_right": ((0,60),(30,60),(60,60),(90,60)),
        }

        self.reset()

    def reset(self):
        # reset all player value
        self.resting = False
        self.dy = 0
        self.dx = 0
        self.is_dead = False
        self.is_moving = False
        self.direction = 1
        self.gun_cooldown = 0
        self.anim = "idle"
        self.anim_frame = 0
        self.anim_pos = None
        self.anim_time = 0

    def update(self, dt, game):
        last = self.rect.copy()

        self.rect.x += self.dx * dt
        if self.dx > 10 or self.dx < -10:
            self.dx *= .8
        else:
            self.dx = 0
            self.is_moving = False

        self.dy = min(400, self.dy + 40)
        self.rect.y += self.dy * dt

        # check if collide with some fruit
        hit_list = pygame.sprite.spritecollide(self, game.fruit_list, False)
        for fruit in hit_list:
            game.fruit_list.remove(fruit)
            game.score.update()
            game.mixer.play_fx("crunch")

            if len(game.fruit_list) == 0:
                game.add_fruit(1)

        # check if collide with enemy
        hit_list = pygame.sprite.spritecollide(self, game.enemy_list, False)
        if hit_list:
            game.mixer.play_fx("no")
            self.is_dead = True
            #~ pass


        new = self.rect
        self.resting = False
        for cell in pygame.sprite.spritecollide(self, game.block_list, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy = 0

        if self.rect.x >= game.width:
            self.rect.x = -15
            game.mixer.play_fx("flip")

        if self.rect.x <= -16:
            self.rect.x = game.width
            game.mixer.play_fx("flip")

        if self.rect.y >= game.height:
            self.rect.y = - 30
            game.mixer.play_fx("flip")

        # set anim
        self.anim_time += dt

        if self.resting and self.is_moving:
            if self.direction:
                self.anim = "walk_left"
            else:
                self.anim = "walk_right"
            if self.anim_time > .1:
                self.anim_frame += 1
                self.anim_time = 0
            if self.anim_frame >= 4:
                self.anim_frame = 0
        elif not self.resting:
            if self.direction:
                self.anim = "jump_left"
            else:
                self.anim = "jump_right"
            if self.dy > 0:
                self.anim_frame = 0
            else:
                self.anim_frame = 1
        else:
            self.anim = "idle"
            self.anim_frame = 0

        self.anim_pos = self.anim_state[self.anim][int(self.anim_frame)]

    def go_left(self):
        self.dx = -200
        self.is_moving = True
        self.direction = 0

    def go_right(self):
        self.dx = 200
        self.is_moving = True
        self.direction = 1

    def jump(self):
        if self.resting:
            self.dy = -500
            self.game.mixer.play_fx("jump")
