import pygame


#Init my game
pygame.init()

#Screen
screen = pygame.display.set_mode((800, 600))

#game loop always on display
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
