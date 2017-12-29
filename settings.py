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
        self.ship_speed_factor = 15
        self.ship_limit = 3

        # 外星人设置
        self.alien_speed_factor = 50
        self.fleet_drop_speed = 10
        # fleet_direciton = 1 turn right, = -1 turn left.
        self.fleet_direciton = 1

        # bullet setting
        self.bullet_speed_factor = 15
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
