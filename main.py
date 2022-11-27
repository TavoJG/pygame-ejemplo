'''
Modulo principal del programa
'''

import random
import sys
import pygame

pygame.mixer.init()
i = 0

room = 1
if room == 1:
    sala = "Matrix pastillas"
    vista1 = pygame.image.load("images/dialogo_morfeo_matrix.jpg")
    vista2 = pygame.image.load("images/morfeo_matrix.png")
    vista3 = pygame.image.load("images/delorean.jpg")
if room == 2:
    sala = "Minecraft"
    variable = 1
    if variable in [1, 2, 3]:
        vista = pygame.image.load("images/minecraft_1.jpeg")
        suceso1 = pygame.mixer.Sound(
            "sounds/minecraft_puerta.mp3")
        suceso1.play()
        if not pygame.mixer.music.get_busy():
            suceso2 = pygame.mixer.Sound("./sounds/vegetta_1.mp3")
            pygame.mixer.Sound.play(suceso2)
    if variable in [4, 5]:
        vista = pygame.image.load("images/minecraft_2.jpeg")
       # suceso=
    if variable in [6, 7]:
        vista = pygame.image.load("images/minecraft_3.jpeg")
        # suceso=
    if variable == 8:
        vista = pygame.image.load("images/minecraft_4.jpeg")
        # suceso=
if room == 3:
    sala = "Maquina del tiempo"
if room == 4:
    sala = "Codigos"
if room == 5:
    sala = "Habitación del terror"
if room == 6:
    sala = "Little Nightmare"
if room == 7:
    sala = "Mucho texto"
if room == 8:
    sala = "Rickroleo"
if room == 9:
    sala = "Calvooo"
if room == 10:
    sala = "Laberinto"  # Susto falso
if room == 11:
    sala = "Bts"
if room == 12:
    sala == "Preguntas"  # Sos arquitecto
if room == 13:
    sala = "sala de cables"  # Acaba el tiempo e impostor te mata
if room == 14:
    sala = "Rollo del dragón"
if room == 15:
    sala = "Yo quiero un heroe"
if room == 16:
    sala = "Preguntas lol"
if room == 17:
    sala = "Is One Piece real?"
if room == 18:
    sala = "Matrix pastillas"
if room == 19:
    sala = "Matrix pastillas"
if room == 20:
    sala = "Matrix pastillas"
if room == 21:
    sala = "Matrix pastillas"
if room == 22:
    sala = "Matrix pastillas"
if room == 23:
    sala = "Matrix pastillas"
if room == 24:
    sala = "Matrix pastillas"

pygame.init()
display_surf = pygame.display.set_mode((500, 400))
pygame.display.set_caption("||--Random room--||")
Fondo1 = pygame.image.load("images/calabozo_fondo_1.jpg")

while True:
    display_surf.blit(Fondo1, (0, 0))
    # if (i < 9):
    if sala == "Matrix pastillas":
        display_surf.blit(vista1, (0, 290))
        display_surf.blit(vista2, (120, 34))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            display_surf.blit(vista3, (120, 34))
        # i=i+1
    for event in pygame.event.get():
        # El evento 256 es la señal de salida
        if event.type == 256:
            pygame.quit()
            sys.exit()
    pygame.display.update()
