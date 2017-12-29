# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # 表示单个外星人的类

    def __init__(self, ai_settings, screen):
        # initial  alien
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # loading alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # aliens
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save aliens point
        self.x = float(self.rect.x)

    def blitme(self):
        # 指定位置绘制外星人
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        # if aliens in the screen edge, return ture.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # turn aliens right or left.
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direciton)
        self.rect.x = self.x
