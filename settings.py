import logging

class Settings(object):

    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):

        """初始化游戏的设置"""

        self.debug_level = logging.DEBUG

        # 游戏窗口输出设置
        # 窗口尺寸
        self.screen_width = 700
        self.screen_height = 400
        # 游戏背景颜色, 颜色是以RGB值指定的
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 0.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
