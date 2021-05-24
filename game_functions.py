import pygame
import sys


def check_events():
    """监视键盘和鼠标事件"""
    # Attention: 一个按键关联一个事件
    # 如果 多个按键同时被操作做(例如 被按下), 会得到多个 event
    for event in pygame.event.get():
        # case: 键盘点击 退出
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, log, screen, alien):
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 更新 Aliens
    update_aliens(alien, log)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_aliens(alien, log):

    if alien.check_edges():
        alien.change_direction()

    log.debug(f'x coordinate of alien: {alien.rect.x} | y coordinate of alien: { alien.rect.y}')
    alien.update_location()

    # 放到屏幕上
    alien.blitme()


