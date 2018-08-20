import pygame
from jingling import *
class PlaneGame(object):
	def __init__(self):
		print('初始化窗口')
		# 1. 创建游戏的窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 2. 创建游戏的时钟
		self.clock = pygame.time.Clock()
		# 3. 调用私有方法，精灵和精灵组的创建
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#定时


	def start_game(self):
		print("开始游戏...")
		while True:
			# 1. 设置刷新帧率
			self.clock.tick(60)
			# 2. 事件监听
			self.__event_handler()
			# 3. 碰撞检测
			self.__check_collide()
			# 4. 更新精灵组
			self.__update_sprites()
			# 5. 更新屏幕显示
			pygame.display.update()


	def __create_sprites(self):
		'''创建精灵'''
		bg1=BackGroundSpriteadds()
		bg2=BackGroundSpriteadds(True)
		self.bg_group=pygame.sprite.Group(bg1,bg2)
		self.enemy_group=pygame.sprite.Group()#创建敌机精灵组		
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
	def __event_handler(self):
		'''监听事件'''
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				planeGame.__game_over()
			elif event.type==CREATE_ENEMY_EVENT:#定时敌机出现
				print('敌机出场')
				self.enemy_group.add( EnemySprite())

	def __check_collide(self):
		'''碰撞检测'''
		pass


	def __update_sprites(self):
		'''更新精灵组'''
		self.bg_group.update()
		self.bg_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
	@staticmethod
	def __game_over():
		'''游戏结束'''
		print('游戏结束')
		pygame.quit()
		exit()

if __name__=='__main__':
	#创建对象
	game=PlaneGame()
	#开始游戏
	game.start_game()

