import pygame
from settings import Settings
import game_functions as gf
from alien import Alien
from logger import Logger


def run_game():

    # 创建一个Settings实例，并将其存储在变量ai_settings, 这个实例包含 尺寸，背景颜色 etc
    ai_settings = Settings()

    # 创建logger
    log = Logger('Alien', ai_settings)

    # 初始化游戏; 创建一个屏幕对象screen; config 游戏的 layout
    pygame.init()

    # implement the settings for layout of game
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien")

    # create an alien
    alien = Alien(ai_settings, screen)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, log, screen, alien)


def test():

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    alien_1 = Alien(ai_settings, screen)
    print(alien_1.ai_settings.fleet_direction)

    alien_1.ai_settings.fleet_direction = 2

    alien_1 = Alien(ai_settings, screen)
    print(alien_1.ai_settings.fleet_direction)

    print(ai_settings.fleet_direction)


if __name__ == "__main__":
    run_game()
    # test()
