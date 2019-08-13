import pygame
from plane_sprite import *

pygame.init()
screen = pygame.display.set_mode((480, 700))
# 加载图片
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (180, 500))
# 图片绘制完成之后统一update,显示最终屏幕的结果
pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(180, 500, 102, 126)

enemy = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png")
enemy_group = pygame.sprite.Group(enemy, enemy2)

while True:
    clock.tick(60)
    if hero_rect.y <= -hero_rect.height:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    hero_rect.y -= 1

    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()

    # event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)
pygame.quit()
