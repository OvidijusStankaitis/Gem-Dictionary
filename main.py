import pygame
from game import Game

pygame.init()
pygame.mixer.init()

################### Icon and name ###################
ICON1 = pygame.image.load('Game Files/Character and Icon/ICON.png')
pygame.display.set_icon(ICON1)
pygame.display.set_caption('GEM DICTONARY')

################### Music ###################
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND1.wav')
pygame.mixer.music.play(-1)
G = Game()

################### Main loop ###################
while G.RUNNING:
    G.CURRENT_MENU.displayMenu()
    G.gameLoop()