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
            print("Entra")
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            print(playerX, playerX_change, playerY, playerY_change)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                playerX_change = 0

    if playerX >= max_screenX or playerX <= 0:
        playerX_change = 0
    if playerY >= max_screenY or playerY <= 0:
        playerY_change = 0
    playerX += playerX_change 
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()