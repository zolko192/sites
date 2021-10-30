import pygame

class Ember(object):
    """ Ember character főosztálya """
    def __init__(self):
        pygame.init()
        self.size = ((800, 600))
        self.screen = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption("Ember")
        self.background = pygame.Color("white")
        self.fps = 60
        self.done = True
        self.drawing = Draw_Ember(self.screen)
        self.x, self.y = self.drawing.x, self.drawing.y
        while self.done == True:
            self.screen.fill(self.background)
            self.x, self.y = self.drawing.x, self.drawing.y
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                    pygame.quit()
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.y += 10
                        print(self.y)
                    if event.key == pygame.K_UP:
                        self.y -= 10
                        print(self.y)
                    if event.key == pygame.K_RIGHT:
                        self.x += 10
                        print(self.x)
                    if event.key == pygame.K_LEFT:
                        self.x -= 10
                        print(self.x)

                self.drawing.circles(self.x, self.y)
                pygame.display.update()

class Draw_Ember(object):
    """ Ember lerajzolása """
    def __init__(self, screen):
        self.screen = screen
        self.red = pygame.Color("red")   
        pygame.draw.rect(self.screen, self.red, (10, 20, 30, 40))
        self.x, self.y = 100, 150
        self.circle = pygame.draw.circle(self.screen, self.red, (self.x, self.y), 10)

    def circles(self, x, y):
        self.x, self.y = x, y
        self.circle = pygame.draw.circle(self.screen, self.red, (self.x, self.y), 10)