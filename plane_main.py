import pygame
from plane_sprite import *


class PlaneGame:
    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.enemys = []
        self.enemy_group = pygame.sprite.Group(self.enemys)

    def __create_sprites(self):
        enemy = GameSprite("./images/enemy1.png")
        self.enemys.append(enemy)
        pass

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

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        print("游戏结束")
        exit()


if __name__ == "__main__":
    plane_game = PlaneGame()
    plane_game.start_game()
