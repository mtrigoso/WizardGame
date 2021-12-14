from pygame.locals import *
import pygame
from Player import Player
import time
import _thread
import random

class App(object):
    windowWidth = 1275
    windowHeight = 500
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._player_surf = None
        self.player = Player()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._player_surf, (self.player.x, self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_init(self):
        pygame.init()
        self.myFont = pygame.font.SysFont("Times New Roman", 24)
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption("Wizard Game")
        self._running = True
        self._player_surf = pygame.image.load("player.png").convert()
        return True

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRightI()

            if (keys[K_LEFT]):
                self.player.moveLeftI()

            if (keys[K_UP]):
                self.player.moveUpI()

            if (keys[K_DOWN]):
                self.player.moveDownI()

            time.sleep(0.05)

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

        self.on_cleanup()
