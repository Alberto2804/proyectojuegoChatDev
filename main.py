import pygame
import sys

# Inicializa Pygame
pygame.init()

# Establece el título de la ventana
pygame.display.set_caption('Qubit Game')

# Define algunos colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Establece la resolución de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Establece la fuente para el texto
fuente = pygame.font.Font(None, 36)

# Variables para el estado del Qubit
estado = '0'
superposicion = False
alternar_color = False
color_actual = AZUL

# Bucle de juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_0:
                estado = '0'
                superposicion = False
                color_actual = AZUL
            elif evento.key == pygame.K_1:
                estado = '1'
                superposicion = False
                color_actual = ROJO
            elif evento.key == pygame.K_SPACE:
                superposicion = True
                alternar_color = True
                color_actual = AZUL

    # Dibuja el fondo
    pantalla.fill(NEGRO)

    # Dibuja el Qubit
    if superposicion:
        if alternar_color:
            color_actual = ROJO
            alternar_color = False
        else:
            color_actual = AZUL
            alternar_color = True
    pygame.draw.circle(pantalla, color_actual, (ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2), 50)

    # Muestra el estado actual
    if superposicion:
        texto_estado = fuente.render('Estado: SUPERPOSICIÓN', True, BLANCO)
    else:
        texto_estado = fuente.render(f'Estado: {estado}', True, BLANCO)
    pantalla.blit(texto_estado, (10, 10))

    # Actualiza la pantalla
    pygame.display.flip()
    pygame.time.Clock().tick(60)
