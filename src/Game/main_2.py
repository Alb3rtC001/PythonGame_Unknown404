import pygame
import sys
import random

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
enemie_img = pygame.image.load("./src/Img/enemie_robot.gif")

DEFAULT_IMAGE_SIZE = (47, 60)
Player_img = pygame.transform.scale(Player_img, DEFAULT_IMAGE_SIZE)
playerX = 300
playerY = 400
playerX_change = 0
playerY_change = 0
player_speed = 1.0

atack_btn = 0
rpm_atack = 8

enemie_img = pygame.transform.scale(enemie_img, DEFAULT_IMAGE_SIZE)
enemieX = random.randint(100, 400)
enemieY = random.randint(100, 300)


#Acabar disparos
def proyectil(pendiente ,subX, Y_fin, Y_ini, X_fin, X_ini):
    if Y_ini == Y_fin or X_ini == subX:
        if Y_ini == Y_fin:
            x = 0
            if subX-X_fin > 0:
                x = subX + 1
                return [Y_ini, x]
            else:
                x = subX - 1
                return [Y_ini, x]
        else:
            y = 0
            if Y_ini-Y_fin > 0:
                y = Y_ini +1
                return [y, X_ini]
            else:
                y = Y_ini -1
                return [y, X_ini]
    else:
        #Seguir por aqui
        y = pendiente*subX + Y_fin
    return [y, subX]

def player(x, y):
    screen.blit(Player_img, (x, y))

def enemie(x, y):
    screen.blit(enemie_img, (x, y))

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
        if(atack_btn == 0):
            #Aquí va el disparo
            print("PIUM!!")
            pendiente = ((event.pos[0] - playerX)/ (event.pos[1] - playerY))
            print("la pendiente es: ", proyectil(pendiente, 0.1, event.pos[1], playerY, event.pos[0], playerX))
        atack_btn += 1
        #print(atack_btn)
        if(atack_btn >= rpm_atack):
            atack_btn = 0
    if event.type == pygame.MOUSEBUTTONUP:
        atack_btn = 0

    # Actualiza las coordenadas del jugador
    playerX += playerX_change
    playerY += playerY_change

    # Limita las coordenadas del jugador dentro de la pantalla
    playerX = max(0, min(playerX, max_screenX - DEFAULT_IMAGE_SIZE[0]))
    playerY = max(0, min(playerY, max_screenY - DEFAULT_IMAGE_SIZE[1]))

    # Dibuja el suelo
    screen.blit(room_flor_img, (0, 0))

    #Dibujar enemigo
    enemie(enemieX, enemieY)

    # Dibuja al jugador
    player(playerX, playerY)

    pygame.display.update()

# Sale del programa
pygame.quit()
sys.exit()
