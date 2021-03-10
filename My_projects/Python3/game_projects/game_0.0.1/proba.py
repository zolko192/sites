import pygame
import configparser

pygame.init()

config = configparser.ConfigParser()
config.read('settings.ini')

sizex, sizey = 800, 600
screen = pygame.display.set_mode((sizex, sizey))
title = pygame.display.set_caption("Térképrács készítése")

white = pygame.Color("white")
black = pygame.Color("black")
green = pygame.Color("green")
blue = pygame.Color("blue")

tile = 20
width, height = 20, 20
margin = 5
grid = [[0 for x in range(10)] for y in range(10)]

grid[5][1] = 1
print (grid)

clock = pygame.time.Clock()
fps = 60
running = True
while running:
    screen.fill(black)
    for row in range(10):
        for column in range(10):
            color = white
            if grid[row][column] == 1:
                color = green
            pygame.draw.rect(screen, color, ((margin + width) * row + margin, (margin + height) * column + margin, width, height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            runnning = False
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect.move(100, 0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[0] // (width + margin)
            column = pos[1] // (height + margin)
            print("Click: ", pos, "\nGrid coordinates: Row: {0} Column: {1}".format(row, column))
            grid[row][column] = 1
            for row in range(10):
                for column in range(10):
                    color = white
                    if grid[row][column] == 1:
                        color = blue
                    pygame.draw.rect(screen, color, ((margin + width) * row + margin, (margin + height) * column + margin, width, height))
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
quit()