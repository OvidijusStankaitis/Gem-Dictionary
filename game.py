import pygame.mixer

from menu import *
import sys
import random


################### Lava pool 1 ###################
class lavaPool1(object):
    OBSTACLE_1 = [pygame.image.load('Game Files/Lava Pool 1/Lava Pool1.png'),
                  pygame.image.load('Game Files/Lava Pool 1/Lava Pool2.png'),
                  pygame.image.load('Game Files/Lava Pool 1/Lava Pool3.png'),
                  pygame.image.load('Game Files/Lava Pool 1/Lava Pool4.png')]

    def __init__(self, x, y, width, height):
        self.O_HEIGHT = height
        self.O_WIDTH = width
        self.O_X = x
        self.O_Y = y
        self.HIT_BOX = (x, y, width, height)
        self.RED = (255, 0, 0)
        self.COUNT = 0

    def draw(self, display):
        self.HIT_BOX = (self.O_X + 10, self.O_Y, self.O_WIDTH, self.O_HEIGHT)
        if self.COUNT >= 32:
            self.COUNT = 0
        display.blit(self.OBSTACLE_1[self.COUNT // 8], (self.O_X, self.O_Y))
        self.COUNT += 1


################### Enemy 1 ###################
class enemy1(object):
    ENEMY1 = [pygame.image.load('Game Files/Enemy 1/Enemy1.png'),
              pygame.image.load('Game Files/Enemy 1/Enemy2.png'),
              pygame.image.load('Game Files/Enemy 1/Enemy3.png'),
              pygame.image.load('Game Files/Enemy 1/Enemy4.png')]

    def __init__(self, x, y, width, height):
        self.O_HEIGHT = height
        self.O_WIDTH = width
        self.O_X = x
        self.O_Y = y
        self.HIT_BOX = (x, y, width, height)
        self.RED = (255, 0, 0)
        self.COUNT = 0

    def draw(self, display):
        self.HIT_BOX = (self.O_X, self.O_Y, self.O_WIDTH, self.O_HEIGHT)
        if self.COUNT >= 64:
            self.COUNT = 0
        display.blit(self.ENEMY1[self.COUNT // 16], (self.O_X, self.O_Y))
        self.COUNT += 1


################### Lava pool 2 ###################
class lavaPool2(object):
    OBSTACLE_1 = [pygame.image.load('Game Files/Lava Pool 2/Lava Pool1.png'),
                  pygame.image.load('Game Files/Lava Pool 2/Lava Pool2.png'),
                  pygame.image.load('Game Files/Lava Pool 2/Lava Pool3.png'),
                  pygame.image.load('Game Files/Lava Pool 2/Lava Pool4.png')]

    def __init__(self, x, y, width, height):
        self.O_HEIGHT = height
        self.O_WIDTH = width
        self.O_X = x
        self.O_Y = y
        self.HIT_BOX = (x, y, width, height)
        self.RED = (255, 0, 0)
        self.COUNT = 0

    def draw(self, display):
        self.HIT_BOX = (self.O_X + 10, self.O_Y, self.O_WIDTH, self.O_HEIGHT)
        if self.COUNT >= 32:
            self.COUNT = 0
        display.blit(self.OBSTACLE_1[self.COUNT // 8], (self.O_X, self.O_Y))
        self.COUNT += 1


################### Enemy 2 ###################
class enemy2(object):
    ENEMY1 = [pygame.image.load('Game Files/Enemy 2/Enemy1.png'),
              pygame.image.load('Game Files/Enemy 2/Enemy2.png'),
              pygame.image.load('Game Files/Enemy 2/Enemy3.png'),
              pygame.image.load('Game Files/Enemy 2/Enemy4.png')]

    def __init__(self, x, y, width, height):
        self.O_HEIGHT = height
        self.O_WIDTH = width
        self.O_X = x
        self.O_Y = y
        self.HIT_BOX = (x, y, width, height)
        self.RED = (255, 0, 0)
        self.COUNT = 0

    def draw(self, display):
        self.HIT_BOX = (self.O_X, self.O_Y, self.O_WIDTH, self.O_HEIGHT)
        if self.COUNT >= 64:
            self.COUNT = 0
        display.blit(self.ENEMY1[self.COUNT // 16], (self.O_X, self.O_Y))
        self.COUNT += 1


################### Lava pool 3 ###################
class lavaPool3(object):
    OBSTACLE_1 = [pygame.image.load('Game Files/Lava Pool 3/Lava Pool1.png'),
                  pygame.image.load('Game Files/Lava Pool 3/Lava Pool2.png'),
                  pygame.image.load('Game Files/Lava Pool 3/Lava Pool3.png'),
                  pygame.image.load('Game Files/Lava Pool 3/Lava Pool4.png')]

    def __init__(self, x, y, width, height):
        self.O_HEIGHT = height
        self.O_WIDTH = width
        self.O_X = x
        self.O_Y = y
        self.HIT_BOX = (x, y, width, height)
        self.RED = (255, 0, 0)
        self.COUNT = 0

    def draw(self, display):
        self.HIT_BOX = (self.O_X + 10, self.O_Y, self.O_WIDTH, self.O_HEIGHT)
        if self.COUNT >= 32:
            self.COUNT = 0
        display.blit(self.OBSTACLE_1[self.COUNT // 8], (self.O_X, self.O_Y))
        self.COUNT += 1


################### Enemy 3 ###################
class enemy3(object):
    ENEMY1 = [pygame.image.load('Game Files/Enemy 3/Enemy1.png'),
              pygame.image.load('Game Files/Enemy 3/Enemy2.png'),
              pygame.image.load('Game Files/Enemy 3/Enemy3.png'),
              pygame.image.load('Game Files/Enemy 3/Enemy4.png')]

    def __init__(self, x, y, width, height):
        self.O_HEIGHT = height
        self.O_WIDTH = width
        self.O_X = x
        self.O_Y = y
        self.HIT_BOX = (x, y, width, height)
        self.RED = (255, 0, 0)
        self.COUNT = 0

    def draw(self, display):
        self.HIT_BOX = (self.O_X, self.O_Y, self.O_WIDTH, self.O_HEIGHT)
        if self.COUNT >= 64:
            self.COUNT = 0
        display.blit(self.ENEMY1[self.COUNT // 16], (self.O_X, self.O_Y))
        self.COUNT += 1


################### Game ###################
class Game():
    #################### Variables ###################
    def __init__(self):
        ################### Screen parameters ###################
        self.WIDTH = 1280
        self.HEIGHT = 720

        ################### Display ###################
        self.DISPLAY = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))#, pygame.FULLSCREEN)

        ################### Player ###################
        self.PLAYER_WIDTH = 300
        self.PLAYER_HEIGHT = 300
        self.PLAYER_Y = (self.HEIGHT - (self.HEIGHT - 592)) - self.PLAYER_HEIGHT
        self.PLAYER_X = (self.WIDTH - 1240)
        self.PLAYER_HITBOX_X = self.PLAYER_X + 180
        self.PLAYER_HITBOX_Y = self.PLAYER_Y + 70
        self.PLAYER_HITBOX_W = 60
        self.PLAYER_HITBOX_H = 230

        ################### Sprite ###################
        self.PLAYER = [pygame.image.load('Game Files/Character and Icon/Standing.png').convert_alpha(),
                       pygame.image.load('Game Files/Character and Icon/Jump.png').convert_alpha(),
                       pygame.image.load('Game Files/Character and Icon/Magic.png').convert_alpha()]

        self.PLAYER_MOVEMENT = [pygame.image.load('Game Files/Character and Icon/FW 1.png').convert_alpha(),
                                pygame.image.load('Game Files/Character and Icon/FW 2.png').convert_alpha(),
                                pygame.image.load('Game Files/Character and Icon/FW 3.png').convert_alpha(),
                                pygame.image.load('Game Files/Character and Icon/FW 4.png').convert_alpha(),]

        self.PLAYER_MAGIC_M = [pygame.image.load('Game Files/Character and Icon/FWM 1.png').convert_alpha(),
                               pygame.image.load('Game Files/Character and Icon/FWM 2.png').convert_alpha(),
                               pygame.image.load('Game Files/Character and Icon/FWM 3.png').convert_alpha(),
                               pygame.image.load('Game Files/Character and Icon/FWM 4.png').convert_alpha()]

        self.PLAYER_COUNT = 0

        ################### Projectile ###################
        self.MAGIC = [pygame.image.load('Game Files/Projectile/Magic Ball 1.png').convert_alpha(),
                      pygame.image.load('Game Files/Projectile/Magic Ball 2.png').convert_alpha(),
                      pygame.image.load('Game Files/Projectile/Magic Ball 3.png').convert_alpha(),
                      pygame.image.load('Game Files/Projectile/Magic Ball 4.png').convert_alpha()]

        self.EXPIMG = [pygame.image.load('Game Files/Explosion/Explosion1.png').convert_alpha(),
                       pygame.image.load('Game Files/Explosion/Explosion2.png').convert_alpha(),
                       pygame.image.load('Game Files/Explosion/Explosion3.png').convert_alpha(),
                       pygame.image.load('Game Files/Explosion/Explosion4.png').convert_alpha(),
                       pygame.image.load('Game Files/Explosion/Explosion5.png').convert_alpha()]

        self.EXPLOSION = False
        self.E_COUNT = 0
        self.SHOOT = False
        self.MAGICC = 0
        self.MAGIC_SPEED = 12
        self.MAGIC_X = self.PLAYER_X + 150
        self.MAGIC_Y = self.PLAYER_Y + 130
        self.MAGIC_HITBOX_X = self.MAGIC_X
        self.MAGIC_HITBOX_Y = self.MAGIC_Y
        self.MAGIC_HITBOX_WIDTH = 50
        self.MAGIC_HITBOX_HEIGHT = 30

        ################### Jump ###################
        self.JUMP_Y = 25
        self.JUMP = False

        ################### Obstacles ####################
        self.OBJECTS = []
        self.OBJECTS1 = []
        self.OBJ_GEN = False
        pygame.time.set_timer(pygame.USEREVENT + 1, random.randrange(2500, 3000))

        ################### FPS ###################
        self.CLOCK = pygame.time.Clock()

        ################### Cutscene/Scrolling background ###################
        self.CUTSCENE_A = True
        self.X = 0
        self.X_COORDINATE = 0

        ################### Menu backgrounds ###################
        self.MAIN_BG = pygame.image.load('Game Files/Menu/MainBG.png').convert()
        self.ENTRANCE_BG = pygame.image.load('Game Files/Menu/EntranceBG.png').convert()
        self.CONTROLS_BG = pygame.image.load('Game Files/Menu/ControlsBG.png').convert()

        ################### Game loop elements ###################
        self.RUNNING = True
        self.PLAYING = False
        self.GAME_STATE = 'RUNNING'
        self.PAUSE_MENU_STATE = 'UNPAUSED'

        ################### Keybindings ###################
        self.MOUSE_BUTTON_L = False

        ################### Fonts ###################
        self.FONT_NAME = 'Game Files/Fonts/8-BIT WONDER.TTF'
        self.CONTROLS_FONT_NAME = 'Game Files/Fonts/Retro Gaming.ttf'

        ################### Colors ###################
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BUTTON_TEXT = (156, 108, 60)
        self.BUTTON = (217, 160, 102)
        self.RED = (255, 0, 0)

        ################### Menu ###################
        self.OPTIONS = optionsMenu(self)
        self.MAIN_MENU = mainMenu(self)
        self.VOLUME = volumeMenu(self)
        self.CONTROLS = controlsMenu(self)
        self.PAUSEM = pauseMenu(self)
        self.NEXT = nextLevel(self)
        self.FAIL = failedLevel(self)
        self.CURRENT_MENU = self.MAIN_MENU
        self.PAUSE_O = True

        ################### Music ###################
        self.MUSIC = True

        ################### Cutscenes ###################
        self.CUT = True
        self.CUTSCENE_1 = pygame.image.load('Game Files/Cutscenes/Cutscene 1.png').convert()
        self.CUTSCENE_2 = pygame.image.load('Game Files/Cutscenes/Cutscene 2.png').convert()
        self.CUTSCENE_3 = pygame.image.load('Game Files/Cutscenes/Cutscene 3.png').convert()
        self.CUTSCENE_4 = pygame.image.load('Game Files/Cutscenes/Cutscene 4.png').convert()
        self.CUTSCENE_5 = pygame.image.load('Game Files/Cutscenes/Cutscene 5.png').convert()

        ################### Levels ###################
        self.LEVEL = 0
        self.NEXT_LEVEL = random.randrange(10, 15)
        print(self.NEXT_LEVEL)
        self.MCOUNT = 0

        ################### Level backgrounds ###################
        # Level 1
        self.LEVEL_1_BG = [pygame.image.load('Game Files/Level 1/Level 1_1.png').convert(),
                           pygame.image.load('Game Files/Level 1/Level 1_2.png').convert(),
                           pygame.image.load('Game Files/Level 1/Level 1_3.png').convert(),
                           pygame.image.load('Game Files/Level 1/Level 1_4.png').convert()]
        # Level 2
        self.LEVEL_2_BG = [pygame.image.load('Game Files/Level 2/Level 2_1.png').convert(),
                           pygame.image.load('Game Files/Level 2/Level 2_2.png').convert(),
                           pygame.image.load('Game Files/Level 2/Level 2_3.png').convert(),
                           pygame.image.load('Game Files/Level 2/Level 2_4.png').convert()]
        # Level 3
        self.LEVEL_3_BG = [pygame.image.load('Game Files/Level 3/Level 3_1.png').convert(),
                           pygame.image.load('Game Files/Level 3/Level 3_2.png').convert(),
                           pygame.image.load('Game Files/Level 3/Level 3_3.png').convert(),
                           pygame.image.load('Game Files/Level 3/Level 3_4.png').convert()]

        self.CURRENT_BG = self.LEVEL_1_BG
        self.COUNT = 0
        self.SPEED = 6
        self.MOVING = False

        ################### Sound effects ###################
        self.BUTTONSOUND = pygame.mixer.Sound('Game Files/Background music and sounds/Button.wav')
        self.JUMPSOUND = pygame.mixer.Sound('Game Files/Background music and sounds/Jump.wav')
        self.MAGICSOUND = pygame.mixer.Sound('Game Files/Background music and sounds/Magic.wav')
        self.EXPLOSIONSOUND = pygame.mixer.Sound('Game Files/Background music and sounds/Explosion.wav')

    ################### Level drawing ###################
    def drawLevels(self):
        ################### Level 1 ###################
        if self.LEVEL == 1:
            self.CURRENT_BG = self.LEVEL_1_BG

        ################### Level 2 ###################
        elif self.LEVEL == 2:
            self.CURRENT_BG = self.LEVEL_2_BG

        ################### Level 3 ###################
        elif self.LEVEL == 4:
            self.CURRENT_BG = self.LEVEL_3_BG

        ################### Blits level backround image in the right position ###################
        if self.COUNT >= 64:
            self.COUNT = 0
        self.DISPLAY.blit(self.CURRENT_BG[self.COUNT // 16],
                          (self.X_COORDINATE - self.CURRENT_BG[self.COUNT // 16].get_rect().width, 0))
        if self.X_COORDINATE < self.WIDTH:
            self.DISPLAY.blit(self.CURRENT_BG[self.COUNT // 16], (self.X_COORDINATE, 0))
        self.COUNT += 1
        pygame.display.update()

    ################### Main loop ###################
    def gameLoop(self):
        while self.PLAYING:
            self.checkEvents()

            ################### Game running ###################
            if self.GAME_STATE == 'RUNNING':

                if self.CUT:
                    if self.LEVEL == 0:
                        self.DISPLAY.fill(self.BLACK)
                        self.drawText('HELLO GREAT ADVENTURER!', 40, self.WIDTH / 2, self.HEIGHT - 620, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('DODGE DEADLY POOLS OF LAVA', 40, self.WIDTH / 2, self.HEIGHT - 520, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('KILL YOUR ENEMIES', 40, self.WIDTH / 2, self.HEIGHT - 420, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('AND ADD GEMS TO YOUR DICTIONARY!', 40, self.WIDTH / 2, self.HEIGHT - 320, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('GOOD LUCK!', 40, self.WIDTH / 2, self.HEIGHT - 220, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('PRESS ENTER TO SEE YOUR GEM DICTIONARY', 20, self.WIDTH / 2, self.HEIGHT - 100, self.CONTROLS_FONT_NAME, self.WHITE)
                    elif self.LEVEL == 1:
                        self.DISPLAY.fill(self.BLACK)
                        self.drawText('LEVEL 1 COMPLETED', 40, self.WIDTH / 2, self.HEIGHT - 620, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('YOU FOUND YOUR FIRST GEM!', 40, self.WIDTH / 2, self.HEIGHT - 520, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('ONLY TWO MORE TO GO!', 40, self.WIDTH / 2, self.HEIGHT - 420, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('EXPLORE FURTHER AND YOU WILL FIND THEM!', 40, self.WIDTH / 2, self.HEIGHT - 320, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('GOOD LUCK!', 40, self.WIDTH / 2, self.HEIGHT - 220, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('PRESS ENTER TO SEE YOUR GEM DICTIONARY', 20, self.WIDTH / 2, self.HEIGHT - 100, self.CONTROLS_FONT_NAME, self.WHITE)
                    elif self.LEVEL == 2:
                        self.DISPLAY.fill(self.BLACK)
                        self.drawText('LEVEL 2 COMPLETED', 40, self.WIDTH / 2, self.HEIGHT - 620, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('THERE IS ONLY ONE GEM LEFT!', 40, self.WIDTH / 2, self.HEIGHT - 520, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('GET TO THE DEEPEST LAYER', 40, self.WIDTH / 2, self.HEIGHT - 420, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('AND YOU WILL FIND IT!', 40, self.WIDTH / 2, self.HEIGHT - 320, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('GOOD LUCK!', 40, self.WIDTH / 2, self.HEIGHT - 220, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('PRESS ENTER TO SEE YOUR GEM DICTIONARY', 20, self.WIDTH / 2, self.HEIGHT - 100, self.CONTROLS_FONT_NAME, self.WHITE)
                    elif self.LEVEL == 3:
                        self.DISPLAY.fill(self.BLACK)
                        self.drawText('ONLY THE LAST GEM REMAINS!', 40, self.WIDTH / 2, self.HEIGHT - 620, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('BEAT THIS DUNGEON', 40, self.WIDTH / 2, self.HEIGHT - 520, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('AND YOUR COLLECTION WILL BE COMPLETE!', 40, self.WIDTH / 2, self.HEIGHT - 420, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('GOOD LUCK!', 40, self.WIDTH / 2, self.HEIGHT - 320, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('PRESS ENTER TO SEE YOUR GEM DICTIONARY', 20, self.WIDTH / 2, self.HEIGHT - 100, self.CONTROLS_FONT_NAME, self.WHITE)
                    elif self.LEVEL == 4:
                        self.DISPLAY.fill(self.BLACK)
                        self.DISPLAY.fill(self.BLACK)
                        self.drawText('YOU FOUND THE LAST ONE!', 40, self.WIDTH / 2, self.HEIGHT - 620, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('CONGRATULATIONS!', 40, self.WIDTH / 2, self.HEIGHT - 520, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('YOUR COLLECTION IS FINALLY COMPLETE!', 40, self.WIDTH / 2, self.HEIGHT - 420, self.CONTROLS_FONT_NAME, self.WHITE)
                        self.drawText('PRESS ENTER TO SEE YOUR GEM DICTIONARY', 20, self.WIDTH / 2, self.HEIGHT - 100, self.CONTROLS_FONT_NAME, self.WHITE)
                    if pygame.key.get_pressed()[pygame.K_RETURN]:
                        self.GAME_STATE = 'WIN'

                else:
                    ################### Levels ###################
                    self.drawLevels()

                    ################### Moves image left ###################
                    if pygame.key.get_pressed()[pygame.K_w]:
                        self.MOVING = True
                        if not self.JUMP:
                            self.SPEED = 6
                        elif self.JUMP:
                            self.SPEED = 10
                        self.moveBG_Left()
                    else:
                        self.MOVING = False
                        self.PLAYER_COUNT = 0

                    ################### Jumps ###################
                    if self.JUMP is False and pygame.key.get_pressed()[pygame.K_SPACE] and self.PLAYER_Y >= 200:
                        if self.MUSIC:
                            pygame.mixer.Sound.play(self.JUMPSOUND)
                        self.JUMP = True
                    if self.JUMP:
                        self.jump()

                    if self.JUMP is False and pygame.mouse.get_pressed(num_buttons = 5) == (1, 0, 0, 0, 0) and self.SHOOT is False:
                        if self.MUSIC:
                            pygame.mixer.Sound.play(self.MAGICSOUND)
                        self.SHOOT = True
                    if self.SHOOT:
                        if self.MAGICC >= 64:
                            self.MAGICC = 0
                        self.DISPLAY.blit(self.MAGIC[self.MAGICC // 16], (self.MAGIC_X, self.MAGIC_Y))
                        self.shoot()
                        self.MAGICC += 1

                    for self.OBJECT in self.OBJECTS:
                        if pygame.key.get_pressed()[pygame.K_w]:
                            self.OBJ_GEN = True
                            if not self.JUMP:
                                self.SPEED = 6
                            elif self.JUMP:
                                self.SPEED = 10
                            self.OBJECT.O_X -= self.SPEED
                        if self.OBJECT.O_X < self.OBJECT.O_WIDTH * -1:
                            self.OBJECTS.pop(self.OBJECTS.index(self.OBJECT))

                        if self.PLAYER_HITBOX_X + self.PLAYER_HITBOX_W >= self.OBJECT.O_X and self.PLAYER_X <= self.OBJECT.O_X + (self.OBJECT.O_WIDTH / 2):
                            if self.OBJECT.O_Y <= self.PLAYER_HITBOX_Y + self.PLAYER_HITBOX_H:
                                self.OBJECTS.clear()
                                self.GAME_STATE = 'LOST'
                                if self.MUSIC:
                                    pygame.mixer.music.set_volume(0.1)
                                    pygame.mixer.music.load('Game Files/Background music and sounds/LOSE.wav')
                                    pygame.mixer.music.play(-1)
                                self.MAGIC_HITBOX_X = self.PLAYER_X + 150
                                self.MAGIC_X = self.PLAYER_X + 300
                                self.SHOOT = False

                    for self.OBJECT1 in self.OBJECTS1:
                        if pygame.key.get_pressed()[pygame.K_w]:
                            self.OBJ_GEN = True
                            if not self.JUMP:
                                self.SPEED = 6
                            elif self.JUMP:
                                self.SPEED = 10
                            self.OBJECT1.O_X -= self.SPEED

                        if self.PLAYER_HITBOX_X + self.PLAYER_HITBOX_W >= self.OBJECT1.O_X and self.PLAYER_X <= self.OBJECT1.O_X + (self.OBJECT1.O_WIDTH / 2):
                            self.OBJECTS.clear()
                            self.OBJECTS1.clear()
                            self.OBJ_GEN = False
                            self.EXPLOSION = False
                            self.GAME_STATE = 'LOST'
                            if self.MUSIC:
                                pygame.mixer.music.set_volume(0.1)
                                pygame.mixer.music.load('Game Files/Background music and sounds/LOSE.wav')
                                pygame.mixer.music.play(-1)
                            self.MAGIC_HITBOX_X = self.PLAYER_X + 150
                            self.MAGIC_X = self.PLAYER_X + 300
                            self.SHOOT = False

                        if self.OBJECT1.O_X < 1280:
                            if self.MAGIC_HITBOX_X >= self.OBJECT1.O_X:
                                if self.MUSIC:
                                    pygame.mixer.Sound.play(self.EXPLOSIONSOUND)
                                self.MAGIC_HITBOX_X = self.PLAYER_X + 150
                                self.EXPLOSION = True
                                self.MAGIC_X = self.PLAYER_X + 300
                                self.SHOOT = False
                                self.MCOUNT += 1

                    ################### Character Movement ####################
                    if not self.JUMP and not self.MOVING and not self.SHOOT:
                        self.DISPLAY.blit(self.PLAYER[0], (self.PLAYER_X, self.PLAYER_Y))

                    ################### Jump ####################
                    elif self.JUMP:
                        self.DISPLAY.blit(self.PLAYER[1], (self.PLAYER_X, self.PLAYER_Y))

                    ################### Walking and shooting ####################
                    elif self.MOVING and self.SHOOT and self.MAGIC_X < (self.WIDTH / 2):
                        if self.PLAYER_COUNT >= 64:
                            self.PLAYER_COUNT = 0
                        self.DISPLAY.blit(self.PLAYER_MAGIC_M[self.PLAYER_COUNT // 16], (self.PLAYER_X, self.PLAYER_Y))
                        self.PLAYER_COUNT += 1

                    ################### Canceling the previous animation ####################
                    elif self.MOVING and self.SHOOT and self.MAGIC_X > (self.WIDTH / 2) - 200:
                        if self.PLAYER_COUNT >= 64:
                            self.PLAYER_COUNT = 0
                        self.DISPLAY.blit(self.PLAYER_MOVEMENT[self.PLAYER_COUNT // 16], (self.PLAYER_X, self.PLAYER_Y))
                        self.PLAYER_COUNT += 1

                    ################### Walking ####################
                    elif self.MOVING:
                        if self.PLAYER_COUNT >= 64:
                            self.PLAYER_COUNT = 0
                        self.DISPLAY.blit(self.PLAYER_MOVEMENT[self.PLAYER_COUNT // 16], (self.PLAYER_X, self.PLAYER_Y))
                        self.PLAYER_COUNT += 1

                    ################### Shooting ####################
                    elif self.SHOOT and self.MAGIC_X < (self.WIDTH / 2) - 200 and not self.MOVING:
                        self.DISPLAY.blit(self.PLAYER[2], (self.PLAYER_X, self.PLAYER_Y))

                    ################### Canceling the previous animation ####################
                    elif self.SHOOT and self.MAGIC_X > (self.WIDTH / 2) - 200 and not self.MOVING:
                        self.DISPLAY.blit(self.PLAYER[0], (self.PLAYER_X, self.PLAYER_Y))

                    ################### Enemies and obstacles ####################
                    for self.OBJECT in self.OBJECTS:
                        self.OBJECT.draw(self.DISPLAY)

                    for self.OBJECT1 in self.OBJECTS1:
                        self.OBJECT1.draw(self.DISPLAY)
                        if self.EXPLOSION:
                            if self.E_COUNT == 15:
                                self.E_COUNT = 0
                                self.OBJECTS1.pop(self.OBJECTS1.index(self.OBJECT1))
                                self.EXPLOSION = False
                            self.DISPLAY.blit(self.EXPIMG[self.E_COUNT // 3], (self.OBJECT1.O_X, self.OBJECT1.O_Y))
                            self.E_COUNT += 1

                    ################### Levels ###################
                    if self.MCOUNT == self.NEXT_LEVEL:
                        self.CUT = True
                        if self.MUSIC:
                            pygame.mixer.music.set_volume(0.1)
                            pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND1.wav')
                            pygame.mixer.music.play(-1)
                        self.OBJECTS.clear()
                        self.OBJECTS1.clear()
                        self.OBJ_GEN = False
                        self.EXPLOSION = False
                    ################### Game pause ###################
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        self.GAME_STATE = 'NOT_RUNNING'

                self.WINDOW.blit(self.DISPLAY, (0, 0))
                pygame.display.update()

            ################### Pause menu ###################
            elif self.GAME_STATE == 'NOT_RUNNING':
                if self.MUSIC:
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND3.wav')
                    pygame.mixer.music.play(-1)
                self.PAUSE_MENU_STATE = 'PAUSED'
                self.CURRENT_MENU = self.PAUSEM
                self.CURRENT_MENU.displayMenu()
                pygame.display.update()
                while self.PAUSE_O == False:
                    self.CURRENT_MENU.displayMenu()
                if self.PAUSE_MENU_STATE == 'UNPAUSED':
                    self.GAME_STATE = 'RUNNING'

            ################### Loose ###################
            elif self.GAME_STATE == 'LOST':
                self.CURRENT_MENU = self.FAIL
                self.CURRENT_MENU.displayMenu()
                pygame.display.update()

            elif self.GAME_STATE == 'WIN':
                self.CURRENT_MENU = self.NEXT
                self.CURRENT_MENU.displayMenu()

            self.resetKeys()
            self.CLOCK.tick(75)

    ################### Events ###################
    def checkEvents(self):
        ################### Checks if X button was pressed ###################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
                self.PLAYING = False
                self.CURRENT_MENU.RUN_DISPLAY = False
                pygame.quit()
                sys.exit()

            ################### Random OBJ GEN ###################
            if event.type == pygame.USEREVENT + 1:
                if pygame.key.get_pressed()[pygame.K_w]:
                    self.RANDOM = random.randrange(0, 4)
                    if self.LEVEL == 1:
                        if self.RANDOM == 0 or self.RANDOM == 2:
                            self.OBJECTS.append(lavaPool1(1280, 584, 225, 120))
                        elif self.RANDOM == 1 or self.RANDOM == 3:
                            self.OBJECTS1.append(enemy1(1280, 292, 300, 300))
                    elif self.LEVEL == 2:
                        if self.RANDOM == 0 or self.RANDOM == 2:
                            self.OBJECTS.append(lavaPool2(1280, 584, 225, 120))
                        elif self.RANDOM == 1 or self.RANDOM == 3:
                            self.OBJECTS1.append(enemy2(1280, 292, 300, 300))
                    elif self.LEVEL == 4:
                        if self.RANDOM == 0 or self.RANDOM == 2:
                            self.OBJECTS.append(lavaPool3(1280, 584, 225, 120))
                        elif self.RANDOM == 1 or self.RANDOM == 3:
                            self.OBJECTS1.append(enemy3(1280, 292, 300, 300))

            ################### Checks for left click ###################
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.MOUSE_BUTTON_L = True

    ################### Resets buttons ###################
    def resetKeys(self):
        self.MOUSE_BUTTON_L = False

    ################### Draws text ###################
    def drawText(self, text, size, x, y, font, color):
        font = pygame.font.Font(font, size)
        TEXT_SURFACE = font.render(text, True, color)
        TEXT_RECT = TEXT_SURFACE.get_rect()
        TEXT_RECT.center = (x, y)
        self.DISPLAY.blit(TEXT_SURFACE, TEXT_RECT)

    ################### Draws buttons ###################
    def drawButtons(self, x, y, width, height):
        pygame.draw.rect(self.DISPLAY, self.BUTTON, pygame.Rect(x, y, width, height))

    ################### Moves background left ###################
    def moveBG_Left(self):
        if self.COUNT >= 64:
            self.COUNT = 0
        self.X_COORDINATE = self.X % self.CURRENT_BG[self.COUNT // 16].get_rect().width
        self.DISPLAY.blit(self.CURRENT_BG[self.COUNT // 16],
                          (self.X_COORDINATE - self.CURRENT_BG[self.COUNT // 16].get_rect().width, 0))
        if self.X_COORDINATE < self.WIDTH:
            self.DISPLAY.blit(self.CURRENT_BG[self.COUNT // 16], (self.X_COORDINATE, 0))
        self.X = self.X - self.SPEED
        self.COUNT += 1

    def jump(self):
        self.PLAYER_Y -= self.JUMP_Y
        self.PLAYER_HITBOX_Y -= self.JUMP_Y
        self.JUMP_Y -= 1
        if self.COUNT >= 64:
            self.COUNT = 0
        self.DISPLAY.blit(self.CURRENT_BG[self.COUNT // 16],
                          (self.X_COORDINATE - self.CURRENT_BG[self.COUNT // 16].get_rect().width, 0))
        if self.X_COORDINATE < self.WIDTH:
            self.DISPLAY.blit(self.CURRENT_BG[self.COUNT // 16], (self.X_COORDINATE, 0))
        self.COUNT += 1
        if self.JUMP_Y < -25:
            self.JUMP = False
            self.JUMP_Y = 25

    def shoot(self):
        self.MAGIC_X += self.MAGIC_SPEED
        self.MAGIC_HITBOX_X += self.MAGIC_SPEED
        if self.MAGIC_X >= 1280:
            self.SHOOT = False
            self.MAGIC_HITBOX_X = self.PLAYER_X + 150
            self.MAGIC_X = self.PLAYER_X + 300