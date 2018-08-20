import pygame
from jinglingzu import *
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self._create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#定时

	def start_game(self):
		while True:
			
			self.clock.tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()
	def __create_sprites(self):#创建精灵组和精灵组
		bg1 = BackGroundSprite()
		bg2 = BackGroundSprite(True)
		self.bg_group = pygame.sprite.Group(bg1,bg2)
		self.enemy_group = pygame.sprite.Group()#创建敌机精灵组

		
	def __event_handler(self):
		#事件监听
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				
				enemy = EnemySprite()
				self.enemy_group.add(enemy)  #通过add方法添加

	def __check_collide(self):
		pass
	def __update_sprites(self):
		self.bg_group.update()
		self.bg_group.draw(self.screen)
		
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

	@staticmethod
	def __game_over():
		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == '__main__':
	game = PlayGame()
	game.start_game()
		
class Hero(GameSprite):	
	def __init(self):
		super().__init__("./images/me1.png",0)
		self.rect.centrx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

