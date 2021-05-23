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


def update_screen(ai_settings, screen, alien):
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 更新 Aliens
    update_aliens(alien)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_aliens(alien):

    print(alien.check_edges())

    if alien.check_edges():
        print('done')
        alien.change_direction()


    print(f'{alien.rect.x} & { alien.rect.y}')

    alien.update_location()

    # 放到屏幕上
    alien.blitme()


