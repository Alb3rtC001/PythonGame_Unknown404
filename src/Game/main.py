import pygame
import sys
#from ..Module.Character import Personaje


#Init my game
pygame.init()


max_screenX = 800
max_screenY = 600
#Screen
screen = pygame.display.set_mode((max_screenX, max_screenY))
pygame.display.set_caption("Unknown404")

#Player
sys.path.insert(0,"..")
Player_img = pygame.image.load("./src/Img/resize_transparent_roboto.png")
# Set the size for the image
DEFAULT_IMAGE_SIZE = (47, 60)
# Scale the image to your needed size
Player_img = pygame.transform.scale(Player_img, DEFAULT_IMAGE_SIZE)
playerX = 300
playerY = 400
playerX_change = 0
playerY_change = 0

#Print player in screen
def player(x, y):
    screen.blit(Player_img, (x, y))

#game loop always on display
running = True
while running:
    screen.fill((100, 200, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if playerY == max_screenY:
                    playerY_change = 1
                else:
                    playerY_change = 0.1
            if event.key == pygame.K_w:
                if playerY == 0:
                    playerY_change -1
                else:
                    playerY_change = -0.1
            if event.key == pygame.K_d:
                if playerX == max_screenX:
                    max_screenX = 1
                else:
                    playerX_change = 0.1
            if event.key == pygame.K_a:
                if playerX == 0:
                    playerX_change = -1
                else:
                    playerX_change = -0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
        print(playerX, playerX_change, playerY, playerY_change)

    playerX += playerX_change 
    playerY += playerY_change
    if playerX >= max_screenX - 47 or playerX <= 0:
        playerX_change = 0
    if playerY >= max_screenY - 60 or playerY <= 0:
        playerY_change = 0
    player(playerX, playerY)
    pygame.display.update()