import pygame
import sys

pygame.init()
pygame.mixer.init()


class Menu():
    #################### Variables ####################
    def __init__(self, game):
        self.game = game
        self.MID_WIDTH = self.game.WIDTH / 2
        self.MID_HEIGHT = self.game.HEIGHT / 2
        self.RUN_DISPLAY = True

    #################### Menu printing ####################
    def blitMenu(self):
        self.game.WINDOW.blit(self.game.DISPLAY, (0, 0))
        pygame.display.update()
        self.game.resetKeys()


class mainMenu(Menu):
    #################### Menu variables ####################
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'START'
        self.STARTX = self.MID_WIDTH - 129
        self.STARTY = self.MID_HEIGHT - 80
        self.OPTIONSX1 = self.MID_WIDTH - 164
        self.OPTIONSY1 = self.MID_HEIGHT - 40
        self.EXITX1 = self.MID_WIDTH - 194
        self.EXITY1 = self.MID_HEIGHT
        self.ENTRANCE = True


    ##################### Visuals ####################
    def displayMenu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.checkEvents()
            if self.ENTRANCE:
                self.game.DISPLAY.fill(self.game.BLACK)
                self.game.DISPLAY.blit(self.game.ENTRANCE_BG, (0, 0))
                self.blitMenu()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.ENTRANCE = False
                    elif event.type == pygame.QUIT:
                        self.game.RUNNING = False
                        self.game.PLAYING = False
                        self.game.CURRENT_MENU.RUN_DISPLAY = False
                        pygame.quit()
                        sys.exit()
            else:
                self.game.DISPLAY.fill(self.game.BLACK)
                self.game.DISPLAY.blit(self.game.MAIN_BG, (0, 0))
                self.game.drawText('MAIN', 25, (self.game.WIDTH / 2) - 183, self.game.HEIGHT / 2 - 160, self.game.FONT_NAME, self.game.WHITE)
                self.game.drawText('MENU', 25, (self.game.WIDTH / 2) - 177, self.game.HEIGHT / 2 - 130, self.game.FONT_NAME, self.game.WHITE)
                self.game.drawButtons(406, 267, 205, 28)
                self.game.drawText('START GAME', 20, self.STARTX, self.STARTY, self.game.FONT_NAME, self.game.BUTTON_TEXT)
                self.game.drawButtons(406, 307, 137, 28)
                self.game.drawText('OPTIONS', 20, self.OPTIONSX1, self.OPTIONSY1, self.game.FONT_NAME, self.game.BUTTON_TEXT)
                self.game.drawButtons(406, 347, 76, 28)
                self.game.drawText('EXIT', 20, self.EXITX1, self.EXITY1, self.game.FONT_NAME, self.game.BUTTON_TEXT)
                self.checkInput()
                self.blitMenu()

    #################### Cursor position ####################
    def cursorPos(self):
        if 611 >= pygame.mouse.get_pos()[0] >= 406 and 295 >= pygame.mouse.get_pos()[1] >= 267:
            self.STATE = 'START'
            self.game.drawText('START GAME', 20, self.STARTX, self.STARTY, self.game.FONT_NAME, self.game.WHITE)
        elif 543 >= pygame.mouse.get_pos()[0] >= 406 and 335 >= pygame.mouse.get_pos()[1] >= 307:
            self.STATE = 'OPTIONS'
            self.game.drawText('OPTIONS', 20, self.OPTIONSX1, self.OPTIONSY1, self.game.FONT_NAME, self.game.WHITE)
        elif 482 >= pygame.mouse.get_pos()[0] >= 406 and 375 >= pygame.mouse.get_pos()[1] >= 347:
            self.STATE = 'EXIT'
            self.game.drawText('EXIT', 20, self.EXITX1, self.EXITY1, self.game.FONT_NAME, self.game.WHITE)
        else:
            self.STATE = 'NOT_ON_BUTTON'

    #################### Inputs ####################
    def checkInput(self):
        self.cursorPos()
        #################### Input Checking ####################
        if self.game.MOUSE_BUTTON_L:
            if self.STATE == 'START':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.PLAYING = True
            elif self.STATE == 'OPTIONS':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.CURRENT_MENU = self.game.OPTIONS
            elif self.STATE == 'EXIT':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                pygame.time.delay(200)
                self.game.RUNNING = False
                self.game.PLAYING = False
                pygame.quit()
                sys.exit()
            elif self.STATE == 'NOT_ON_BUTTON':
                return
            self.RUN_DISPLAY = False


class optionsMenu(Menu):
    #################### Menu variables ####################
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'VOLUME'
        self.VOLX = self.MID_WIDTH - 163
        self.VOLY = self.MID_HEIGHT - 80
        self.CONTROLSX = self.MID_WIDTH - 149
        self.CONTROLSY = self.MID_HEIGHT - 40
        self.BACKX1 = self.MID_WIDTH - 189
        self.BACKY1 = self.MID_HEIGHT

    #################### Visuals ####################
    def displayMenu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.checkEvents()
            self.game.DISPLAY.fill(self.game.BLACK)
            self.game.DISPLAY.blit(self.game.MAIN_BG, (0, 0))
            self.game.drawText('OPTIONS', 35, (self.game.WIDTH / 2) - 120, self.game.HEIGHT / 2 - 140, self.game.FONT_NAME, self.game.WHITE)
            self.game.drawButtons(406, 267, 137, 28)
            self.game.drawText('VOLUME', 20, self.VOLX, self.VOLY, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.game.drawButtons(406, 307, 166, 28)
            self.game.drawText('CONTROLS', 20, self.CONTROLSX, self.CONTROLSY, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.game.drawButtons(406, 347, 87, 28)
            self.game.drawText('BACK', 20, self.BACKX1, self.BACKY1, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.checkInput()
            self.blitMenu()

    #################### Cursor position ####################
    def cursorPos(self):
        if 543 >= pygame.mouse.get_pos()[0] >= 406 and 295 >= pygame.mouse.get_pos()[1] >= 267:
            self.STATE = 'VOLUME'
            self.game.drawText('VOLUME', 20, self.VOLX, self.VOLY, self.game.FONT_NAME, self.game.WHITE)
        elif 572 >= pygame.mouse.get_pos()[0] >= 406 and 335 >= pygame.mouse.get_pos()[1] >= 307:
            self.STATE = 'CONTROLS'
            self.game.drawText('CONTROLS', 20, self.CONTROLSX, self.CONTROLSY, self.game.FONT_NAME, self.game.WHITE)
        elif 493 >= pygame.mouse.get_pos()[0] >= 406 and 375 >= pygame.mouse.get_pos()[1] >= 347:
            self.STATE = 'BACK'
            self.game.drawText('BACK', 20, self.BACKX1, self.BACKY1, self.game.FONT_NAME, self.game.WHITE)
        else:
            self.STATE = 'NOT_ON_BUTTON'

    #################### Inputs ####################
    def checkInput(self):
        self.cursorPos()
        #################### Input Checking ####################
        if self.game.MOUSE_BUTTON_L:
            if self.STATE == 'VOLUME':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.CURRENT_MENU = self.game.VOLUME
                self.RUN_DISPLAY = False
            elif self.STATE == 'CONTROLS':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.CURRENT_MENU = self.game.CONTROLS
                self.RUN_DISPLAY = False
            elif self.STATE == 'BACK':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                if self.game.PLAYING:
                    self.game.CURRENT_MENU = self.game.PAUSEM
                else:
                    self.game.CURRENT_MENU = self.game.MAIN_MENU
                self.RUN_DISPLAY = False
            elif self.STATE == 'NOT_ON_BUTTON':
                return
            self.RUN_DISPLAY = False


class volumeMenu(Menu):
    #################### Menu variables ####################
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'ON'
        self.ONX = self.MID_WIDTH - 209
        self.ONY = self.MID_HEIGHT - 80
        self.OFFX = self.MID_WIDTH - 199
        self.OFFY = self.MID_HEIGHT - 40
        self.BACKX2 = self.MID_WIDTH - 189
        self.BACKY2 = self.MID_HEIGHT

    #################### Visuals ####################
    def displayMenu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.checkEvents()
            self.game.DISPLAY.fill(self.game.BLACK)
            self.game.DISPLAY.blit(self.game.MAIN_BG, (0, 0))
            self.game.drawText('VOLUME', 35, (self.game.WIDTH / 2) - 120, self.game.HEIGHT / 2 - 140, self.game.FONT_NAME, self.game.WHITE)
            self.game.drawButtons(406, 267, 46, 28)
            self.game.drawText('ON', 20, self.ONX, self.ONY, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.game.drawButtons(406, 307, 67, 28)
            self.game.drawText('OFF', 20, self.OFFX, self.OFFY, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.game.drawButtons(406, 347, 87, 28)
            self.game.drawText('BACK', 20, self.BACKX2, self.BACKY2, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.checkInput()
            self.blitMenu()

    #################### Cursor position ####################
    def cursorPos(self):
        if 452 >= pygame.mouse.get_pos()[0] >= 406 and 295 >= pygame.mouse.get_pos()[1] >= 267:
            self.STATE = 'ON'
            self.game.drawText('ON', 20, self.ONX, self.ONY, self.game.FONT_NAME, self.game.WHITE)
        elif 473 >= pygame.mouse.get_pos()[0] >= 406 and 335 >= pygame.mouse.get_pos()[1] >= 307:
            self.STATE = 'OFF'
            self.game.drawText('OFF', 20, self.OFFX, self.OFFY, self.game.FONT_NAME, self.game.WHITE)
        elif 493 >= pygame.mouse.get_pos()[0] >= 406 and 375 >= pygame.mouse.get_pos()[1] >= 347:
            self.game.drawText('BACK', 20, self.BACKX2, self.BACKY2, self.game.FONT_NAME, self.game.WHITE)
            self.STATE = 'BACK'
        else:
            self.STATE = 'NOT_ON_BUTTON'

    #################### Inputs ####################
    def checkInput(self):
        self.cursorPos()
        #################### Input Checking ####################
        if self.game.MOUSE_BUTTON_L:
            if self.STATE == 'ON':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                if self.game.PLAYING:
                    if self.game.MUSIC:
                        pass
                    else:
                        self.game.MUSIC = True
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play(-1)
                else:
                    if self.game.MUSIC:
                        pass
                    else:
                        self.game.MUSIC = True
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND1.wav')
                        pygame.mixer.music.play(-1)
            elif self.STATE == 'OFF':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.MUSIC = False
                pygame.mixer.music.stop()
            elif self.STATE == 'BACK':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.CURRENT_MENU = self.game.OPTIONS
                self.RUN_DISPLAY = False
            elif self.STATE == 'NOT_ON_BUTTON':
                return
            self.RUN_DISPLAY = False


class controlsMenu(Menu):
    #################### Menu variables ####################
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'BACK3'
        self.BACKX3 = self.MID_WIDTH
        self.BACKY3 = self.MID_HEIGHT + 133
        self.WX = self.MID_WIDTH
        self.WY = self.MID_HEIGHT - 100
        self.SPACEX = self.MID_WIDTH
        self.SPACEY = self.MID_HEIGHT - 40
        self.MOUSELX = self.MID_WIDTH
        self.MOUSELY = self.MID_HEIGHT + 20
        self.ESCX = self.MID_WIDTH
        self.ESCY = self.MID_HEIGHT + 80

    #################### Visuals ####################
    def displayMenu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.checkEvents()
            self.game.DISPLAY.fill(self.game.BLACK)
            self.game.DISPLAY.blit(self.game.CONTROLS_BG, (0, 0))
            self.game.drawText('CONTROLS', 35, self.game.WIDTH / 2, self.game.HEIGHT / 2 - 170, self.game.FONT_NAME, self.game.WHITE)
            self.game.drawText('W - MOVE FORWARD', 20, self.WX, self.WY, self.game.CONTROLS_FONT_NAME, self.game.WHITE)
            self.game.drawText('SPACE - JUMP', 20, self.SPACEX, self.SPACEY, self.game.CONTROLS_FONT_NAME, self.game.WHITE)
            self.game.drawText('LEFT CLICK - ATTACK', 20, self.MOUSELX, self.MOUSELY, self.game.CONTROLS_FONT_NAME, self.game.WHITE)
            self.game.drawText('ESC - PAUSE', 20, self.ESCX, self.ESCY, self.game.CONTROLS_FONT_NAME, self.game.WHITE)
            self.game.drawButtons(595, 480, 87, 28)
            self.game.drawText('BACK', 20, self.BACKX3, self.BACKY3, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.checkInput()
            self.blitMenu()

    #################### Cursor position ####################
    def cursorPos(self):
        if 682 >= pygame.mouse.get_pos()[0] >= 595 and 508 >= pygame.mouse.get_pos()[1] >= 480:
            self.STATE = 'BACK'
            self.game.drawText('BACK', 20, self.BACKX3, self.BACKY3, self.game.FONT_NAME, self.game.WHITE)
        else:
            self.STATE = 'NOT_ON_BUTTON'

    #################### Inputs ####################
    def checkInput(self):
        self.cursorPos()
        #################### Input Checking ####################
        if self.game.MOUSE_BUTTON_L:
            if self.STATE == 'BACK':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.CURRENT_MENU = self.game.OPTIONS
                self.RUN_DISPLAY = False
            elif self.STATE == 'NOT_ON_BUTTON':
                return
            self.RUN_DISPLAY = False


class pauseMenu(Menu):
    #################### Menu variables ####################
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'RESUME'
        self.RESUMEX = self.MID_WIDTH - 164
        self.RESUMEY = self.MID_HEIGHT - 80
        self.OPTIONSX2 = self.MID_WIDTH - 164
        self.OPTIONSY2 = self.MID_HEIGHT - 40
        self.EXITX2 = self.MID_WIDTH - 194
        self.EXITY2 = self.MID_HEIGHT

    #################### Visuals ####################
    def displayMenu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.checkEvents()
            self.game.DISPLAY.fill(self.game.BLACK)
            self.game.DISPLAY.blit(self.game.MAIN_BG, (0, 0))
            self.game.drawText('PAUSED', 35, (self.game.WIDTH / 2) - 128, self.game.HEIGHT / 2 - 140, self.game.FONT_NAME, self.game.WHITE)
            self.game.drawButtons(406, 267, 137, 28)
            self.game.drawText('RESUME', 20, self.RESUMEX, self.RESUMEY, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.game.drawButtons(406, 307, 137, 28)
            self.game.drawText('OPTIONS', 20, self.OPTIONSX2, self.OPTIONSY2, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.game.drawButtons(406, 347, 76, 28)
            self.game.drawText('EXIT', 20, self.EXITX2, self.EXITY2, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.checkInput()
            self.blitMenu()

    #################### Cursor position ####################
    def cursorPos(self):
        if 543 >= pygame.mouse.get_pos()[0] >= 406 and 295 >= pygame.mouse.get_pos()[1] >= 267:
            self.STATE = 'RESUME'
            self.game.drawText('RESUME', 20, self.RESUMEX, self.RESUMEY, self.game.FONT_NAME, self.game.WHITE)
        elif 543 >= pygame.mouse.get_pos()[0] >= 406 and 335 >= pygame.mouse.get_pos()[1] >= 307:
            self.STATE = 'OPTIONS'
            self.game.drawText('OPTIONS', 20, self.OPTIONSX2, self.OPTIONSY2, self.game.FONT_NAME, self.game.WHITE)
        elif 482 >= pygame.mouse.get_pos()[0] >= 406 and 375 >= pygame.mouse.get_pos()[1] >= 347:
            self.STATE = 'EXIT'
            self.game.drawText('EXIT', 20, self.EXITX2, self.EXITY2, self.game.FONT_NAME, self.game.WHITE)
        else:
            self.STATE = 'NOT_ON_BUTTON'

    #################### Inputs ####################
    def checkInput(self):
        self.cursorPos()
        #################### Input Checking ####################
        if self.game.MOUSE_BUTTON_L:
            if self.STATE == 'RESUME':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                if self.game.MUSIC:
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND2.wav')
                    pygame.mixer.music.play(-1)
                self.game.PAUSE_MENU_STATE = 'UNPAUSED'
                self.game.PAUSE_O = True
                if self.game.OBJ_GEN:
                    for self.OBJECT in self.game.OBJECTS:
                        if self.game.OBJECT.O_X >= 1280:
                            self.game.OBJECTS.pop(self.game.OBJECTS.index(self.game.OBJECT))
                    for self.OBJECT1 in self.game.OBJECTS1:
                        if self.game.OBJECT1.O_X >= 1280:
                            self.game.OBJECTS1.pop(self.game.OBJECTS.index(self.game.OBJECT))
            elif self.STATE == 'OPTIONS':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.PAUSE_O = False
                self.game.CURRENT_MENU = self.game.OPTIONS
            elif self.STATE == 'EXIT':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                if self.game.MUSIC:
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND1.wav')
                    pygame.mixer.music.play(-1)
                self.game.PLAYING = False
                self.game.CURRENT_MENU = self.game.MAIN_MENU
                self.game.PAUSE_O = True
                self.game.PAUSE_MENU_STATE = 'UNPAUSED'
                self.game.X = 0
                self.game.X_COORDINATE = 0
                self.game.JUMP = False
                self.game.JUMP_Y = 25
                self.game.PLAYER_Y = (self.game.HEIGHT - (self.game.HEIGHT - 592)) - self.game.PLAYER_HEIGHT
                self.game.PLAYER_HITBOX_Y = self.game.PLAYER_Y + 70
                self.game.LEVEL = 0
                self.game.MCOUNT = 0
                self.game.CUT = True
                self.game.OBJECTS.clear()
                self.game.GAME_STATE = 'RUNNING'
            elif self.STATE == 'NOT_ON_BUTTON':
                return
            self.RUN_DISPLAY = False


class nextLevel(Menu):
    #################### Menu variables ####################
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'NEXT'
        self.NEXT_LEVEL_X = self.MID_WIDTH
        self.NEXT_LEVEL_Y = self.MID_HEIGHT + 230
        self.EXITX3 = self.MID_WIDTH
        self.EXITY3 = self.MID_HEIGHT + 270
        self.LAST = True

    def displayMenu(self):
        self.game.checkEvents()
        if self.game.LEVEL == 0:
            self.game.DISPLAY.blit(self.game.CUTSCENE_1, (0, 0))
        elif self.game.LEVEL == 1:
            self.game.DISPLAY.blit(self.game.CUTSCENE_2, (0, 0))
        elif self.game.LEVEL == 2:
            self.game.DISPLAY.blit(self.game.CUTSCENE_3, (0, 0))
        elif self.game.LEVEL == 3:
            self.game.DISPLAY.blit(self.game.CUTSCENE_4, (0, 0))
        elif self.game.LEVEL == 4:
            self.game.DISPLAY.blit(self.game.CUTSCENE_5, (0, 0))
        if self.game.LEVEL <= 3:
            self.game.drawButtons(530, 577, 215, 28)
            self.game.drawText('START LEVEL', 20, self.NEXT_LEVEL_X, self.NEXT_LEVEL_Y, self.game.FONT_NAME, self.game.BUTTON_TEXT)
            self.game.drawButtons(600, 617, 76, 28)
            self.game.drawText('EXIT', 20, self.EXITX3, self.EXITY3, self.game.FONT_NAME, self.game.BUTTON_TEXT)
        elif self.game.LEVEL == 4:
            self.game.drawButtons(600, 592, 76, 28)
            self.game.drawText('EXIT', 20, self.EXITX3, self.EXITY3 - 25, self.game.FONT_NAME, self.game.BUTTON_TEXT)
        self.checkInput()
        self.blitMenu()

    def cursorPos(self):
        if self.game.LEVEL <= 3:
            if 745 >= pygame.mouse.get_pos()[0] >= 530 and 605 >= pygame.mouse.get_pos()[1] >= 577:
                self.STATE = 'NEXT'
                self.game.drawText('START LEVEL', 20, self.NEXT_LEVEL_X, self.NEXT_LEVEL_Y, self.game.FONT_NAME, self.game.WHITE)
            elif 676 >= pygame.mouse.get_pos()[0] >= 600 and 645 >= pygame.mouse.get_pos()[1] >= 617:
                self.STATE = 'EXIT'
                self.game.drawText('EXIT', 20, self.EXITX3, self.EXITY3, self.game.FONT_NAME, self.game.WHITE)
            else:
                self.STATE = 'NOT_ON_BUTTON'
        elif self.game.LEVEL == 4:
            if 676 >= pygame.mouse.get_pos()[0] >= 600 and 620 >= pygame.mouse.get_pos()[1] >= 592:
                self.STATE = 'EXIT'
                self.game.drawText('EXIT', 20, self.EXITX3, self.EXITY3 - 25, self.game.FONT_NAME, self.game.WHITE)
            else:
                self.STATE = 'NOT_ON_BUTTON'

    def checkInput(self):
        self.cursorPos()
        if self.game.MOUSE_BUTTON_L and self.game.LEVEL <= 3:
            if self.STATE == 'NEXT':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                if self.game.LEVEL == 0:
                    if self.game.MUSIC:
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND2.wav')
                        pygame.mixer.music.play(-1)
                    self.game.GAME_STATE = 'RUNNING'
                    self.game.CUT = False
                    self.game.LEVEL = 1
                elif self.game.LEVEL == 1:
                    if self.game.MUSIC:
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND2.wav')
                        pygame.mixer.music.play(-1)
                    self.game.GAME_STATE = 'RUNNING'
                    self.game.CUT = False
                    self.game.LEVEL = 2
                    self.game.X = 0
                    self.game.X_COORDINATE = 0
                    self.game.JUMP = False
                    self.game.JUMP_Y = 25
                    self.game.PLAYER_Y = (self.game.HEIGHT - (self.game.HEIGHT - 592)) - self.game.PLAYER_HEIGHT
                    self.game.PLAYER_HITBOX_Y = self.game.PLAYER_Y + 70
                    self.game.MCOUNT = 0
                    self.game.OBJECTS.clear()
                    self.game.OBJECTS1.clear()
                elif self.game.LEVEL == 2:
                    self.game.GAME_STATE = 'RUNNING'
                    self.game.CUT = True
                    self.game.LEVEL = 3
                    self.game.X = 0
                    self.game.X_COORDINATE = 0
                    self.game.JUMP = False
                    self.game.JUMP_Y = 25
                    self.game.PLAYER_Y = (self.game.HEIGHT - (self.game.HEIGHT - 592)) - self.game.PLAYER_HEIGHT
                    self.game.PLAYER_HITBOX_Y = self.game.PLAYER_Y + 70
                    self.game.MCOUNT = 0
                    self.game.OBJECTS.clear()
                    self.game.OBJECTS1.clear()
                elif self.game.LEVEL == 3:
                    if self.game.MUSIC:
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND2.wav')
                        pygame.mixer.music.play(-1)
                    self.game.GAME_STATE = 'RUNNING'
                    self.game.CUT = False
                    self.game.LEVEL = 4
                    self.game.X = 0
                    self.game.X_COORDINATE = 0
                    self.game.JUMP = False
                    self.game.JUMP_Y = 25
                    self.game.PLAYER_Y = (self.game.HEIGHT - (self.game.HEIGHT - 592)) - self.game.PLAYER_HEIGHT
                    self.game.PLAYER_HITBOX_Y = self.game.PLAYER_Y + 70
                    self.game.MCOUNT = 0
                    self.game.OBJECTS.clear()
                    self.game.OBJECTS1.clear()
            elif self.STATE == 'EXIT':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                if self.game.MUSIC:
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND1.wav')
                    pygame.mixer.music.play(-1)
                self.game.PLAYING = False
                self.game.CURRENT_MENU = self.game.MAIN_MENU
                self.game.PAUSE_O = True
                self.game.PAUSE_MENU_STATE = 'UNPAUSED'
                self.game.X = 0
                self.game.X_COORDINATE = 0
                self.game.JUMP = False
                self.game.JUMP_Y = 25
                self.game.PLAYER_Y = (self.game.HEIGHT - (self.game.HEIGHT - 592)) - self.game.PLAYER_HEIGHT
                self.game.PLAYER_HITBOX_Y = self.game.PLAYER_Y + 70
                self.game.LEVEL = 0
                self.game.MCOUNT = 0
                self.game.OBJECTS.clear()
                self.game.OBJECTS1.clear()
                self.game.GAME_STATE = 'RUNNING'
            elif self.STATE == 'NOT_ON_BUTTON':
                return
            self.RUN_DISPLAY = False
        if self.game.MOUSE_BUTTON_L and self.game.LEVEL == 4:
            if self.STATE == 'EXIT':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                self.game.PLAYING = False
                self.game.CURRENT_MENU = self.game.MAIN_MENU
                self.game.PAUSE_O = True
                self.game.PAUSE_MENU_STATE = 'UNPAUSED'
                self.game.X = 0
                self.game.X_COORDINATE = 0
                self.game.JUMP = False
                self.game.JUMP_Y = 25
                self.game.PLAYER_Y = (self.game.HEIGHT - (self.game.HEIGHT - 592)) - self.game.PLAYER_HEIGHT
                self.game.PLAYER_HITBOX_Y = self.game.PLAYER_Y + 70
                self.game.LEVEL = 0
                self.game.MCOUNT = 0
                self.game.OBJECTS.clear()
                self.game.OBJECTS1.clear()
                self.game.GAME_STATE = 'RUNNING'
            elif self.STATE == 'NOT_ON_BUTTON':
                return
            self.RUN_DISPLAY = False


class failedLevel(Menu):
    #################### Menu variables ####################
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'RETRY'
        self.YOU_DIED_X = self.MID_WIDTH
        self.YOU_DIED_Y = self.MID_HEIGHT
        self.RETRYX = self.MID_WIDTH
        self.RETRYY = self.MID_HEIGHT + 100

    def displayMenu(self):
        self.game.checkEvents()
        self.game.DISPLAY.fill(self.game.BLACK)
        self.game.drawText('YOU DIED', 50, self.YOU_DIED_X, self.YOU_DIED_Y, self.game.FONT_NAME, self.game.RED)
        self.game.drawText('RETRY', 20, self.RETRYX, self.RETRYY, self.game.FONT_NAME, self.game.WHITE)
        self.checkInput()
        self.blitMenu()

    def cursorPos(self):
        if 686 >= pygame.mouse.get_pos()[0] >= 589 and 470 >= pygame.mouse.get_pos()[1] >= 452:
            self.STATE = 'RETRY'
            self.game.drawText('RETRY', 20, self.RETRYX, self.RETRYY, self.game.FONT_NAME, self.game.RED)
        else:
            self.STATE = 'NOT_ON_BUTTON'

    def checkInput(self):
        self.cursorPos()
        if self.game.MOUSE_BUTTON_L:
            if self.STATE == 'RETRY':
                pygame.mixer.Sound.play(self.game.BUTTONSOUND)
                if self.game.MUSIC:
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.load('Game Files/Background music and sounds/BACKGROUND2.wav')
                    pygame.mixer.music.play(-1)
                self.game.GAME_STATE = 'RUNNING'
                self.game.X = 0
                self.game.X_COORDINATE = 0
                self.game.JUMP = False
                self.game.JUMP_Y = 25
                self.game.PLAYER_Y = (self.game.HEIGHT - (self.game.HEIGHT - 592)) - self.game.PLAYER_HEIGHT
                self.game.PLAYER_HITBOX_Y = self.game.PLAYER_Y + 70
                self.game.MCOUNT = 0
                self.game.OBJECTS.clear()
                self.game.OBJECTS1.clear()
                self.game.GAME_STATE = 'RUNNING'
            elif self.STATE == 'NOT_ON_BUTTON':
                return
            self.RUN_DISPLAY = False