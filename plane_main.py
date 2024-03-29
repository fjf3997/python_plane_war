import pygame
from plane_sprite import *


class PlaneGame:
    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        # print("游戏开始")
        # bg = pygame.image.load("./images/background.png")
        # self.screen.blit(bg, (0, 0))
        # hero = pygame.image.load("./images/me1.png")
        # self.screen.blit(hero, (180, 500))
        # hero_rect = pygame.Rect(180, 500, 102, 126)
        # pygame.init()
        while True:
            # if hero_rect.y <= -hero_rect.height:
            #     hero_rect.y = 700
            # self.screen.blit(bg, (0, 0))
            # self.screen.blit(hero, hero_rect)
            # hero_rect.y -= 1
            # 设置刷新频率
            self.clock.tick(FRAME_PER_SECOND)
            # 时间监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出现")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            # self.hero.rect.x += 5
            self.hero.speed = 5
            # print("向右移动")
        elif key_pressed[pygame.K_LEFT]:
            # self.hero.rect.x -= 5
            self.hero.speed = -5
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        print("游戏结束")
        exit()


if __name__ == "__main__":
    plane_game = PlaneGame()
    plane_game.start_game()
