import pygame

class Menu:

    index = 0
    mode = "menu"

    def __init__(self, game):

        self.game = game

        self.image = pygame.image.load('./images/bg.png')
        self.surf_ind = pygame.Surface([game.width, 80])
        self.surf_ind.set_alpha(128)
        self.surf_ind.fill((0, 0, 0))

        self.game_name = game.font.render("SUPER FRUIT PIE", 1, (255, 255, 255))
        self.game_name_shadow = game.font.render("SUPER FRUIT PIE", 1, (0, 0, 0))

        self.menu_items = [
            game.font.render("PLAY", 1, (255, 255, 255)),
            game.font.render("OPTIONS", 1, (255, 255, 255)),
            game.font.render("CREDITS", 1, (255, 255, 255)),
            game.font.render("QUIT", 1, (255, 255, 255))
            ]

        self.menu_items_shadow = [
            game.font.render("PLAY", 1, (0, 0, 0)),
            game.font.render("OPTIONS", 1, (0, 0, 0)),
            game.font.render("CREDITS", 1, (0, 0, 0)),
            game.font.render("QUIT", 1, (0, 0, 0))
            ]

    def run(self):

        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.mode == "menu":
                            running = False
                        else:
                            self.mode = "menu"
                            self.index = 0
                    elif event.key == pygame.K_UP:
                        if self.index > 0:
                            self.index -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.index < 3:
                            self.index += 1
                    elif event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:

                        # quit
                        if self.mode == "menu" and self.index == 3:
                            running = False
                        # play -> select map
                        elif self.mode == "menu" and self.index == 0:
                            #~ self.mode = "map"
                            self.game.run()
                        # options
                        elif self.mode == "menu" and self.index == 1:
                            pass
                            #~ self.mode = "options"

                        #~ self.game.run()

            if running:
                self.draw()

    def draw(self):
        # draw bg
        self.game.screen.blit(self.image, (0, 0))
        # draw game name
        self.game.screen.blit(self.game_name_shadow, (104, 4))
        self.game.screen.blit(self.game_name, (100, 0))

        if self.mode == "menu":
            self.game.screen.blit(self.surf_ind, (0, self.index * 80 + 100))
            for ind in range(4):
                self.game.screen.blit(self.menu_items_shadow[ind], (204, 104 + ind * 80))
                self.game.screen.blit(self.menu_items[ind], (200, 100 + ind * 80))
        elif self.mode == "map":
            pass
        elif self.mode == "options":
            pass

        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()
