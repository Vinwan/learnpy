# -*- coding: utf-8 -*-

class Settings():

    # 存储外星人入侵的所有设置的类

    def __init__(self):
        # 初始化游戏的设置

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 外星人设置
        self.fleet_drop_speed = 10


        # bullet setting
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # how to update game process
        self.speedup_scale = 1.1

        # update alien score
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # inital seting in game running
        self.ship_speed_factor = 15
        self.bullet_speed_factor = 15
        self.alien_speed_factor = 10

        # fleet_direciton = 1 turn right, = -1 turn left.
        self.fleet_direciton = 1

        # record score
        self.alien_points = 50

    def increase_speed(self):
        # update speed setting
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
