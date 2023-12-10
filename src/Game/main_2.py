import pygame
import sys

# Inicializa pygame
pygame.init()

max_screenX = 620
max_screenY = 600

# Screen
screen = pygame.display.set_mode((max_screenX, max_screenY))
pygame.display.set_caption("Unknown404")

# Imagenes
sys.path.insert(0, "..")
Player_img = pygame.image.load("./src/Img/resize_transparent_roboto.png")
room_flor_img = pygame.image.load("./src/Img/floor.png")

DEFAULT_IMAGE_SIZE = (47, 60)
Player_img = pygame.transform.scale(Player_img, DEFAULT_IMAGE_SIZE)
playerX = 300
playerY = 400
playerX_change = 0
playerY_change = 0
player_speed = 1.0
test = 0

def player(x, y):
    screen.blit(Player_img, (x, y))

# Bucle principal
running = True
keys_pressed = {}
#Restricción de fotogramas y movimiento
clock = pygame.time.Clock()

while running:

    clock.tick(144)
    screen.fill((100, 200, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            keys_pressed[event.key] = False

    # Movimiento basado en las teclas presionadas
    if keys_pressed.get(pygame.K_s):
        playerY_change = player_speed
    elif keys_pressed.get(pygame.K_w):
        playerY_change = -player_speed
    else:
        playerY_change = 0

    if keys_pressed.get(pygame.K_d):
        playerX_change = player_speed
    elif keys_pressed.get(pygame.K_a):
        playerX_change = -player_speed
    else:
        playerX_change = 0

    #Evento pilla el tiempo pulsado left click
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        test += 1
        print(test)
        if(test >= 10):
            test = 0

    # Actualiza las coordenadas del jugador
    playerX += playerX_change
    playerY += playerY_change

    # Limita las coordenadas del jugador dentro de la pantalla
    playerX = max(0, min(playerX, max_screenX - DEFAULT_IMAGE_SIZE[0]))
    playerY = max(0, min(playerY, max_screenY - DEFAULT_IMAGE_SIZE[1]))

    # Dibuja el suelo
    screen.blit(room_flor_img, (0, 0))

    # Dibuja al jugador
    player(playerX, playerY)

    pygame.display.update()

# Sale del programa
pygame.quit()
sys.exit()
