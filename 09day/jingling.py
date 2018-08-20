import random
import pygame

		
SCREEN_RECT=pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT#常量
class GameSprite(pygame.sprite.Sprite):#父类
	def __init__(self,imagename,speed=1):
		
		super().__init__()#调用父类方法
	
		self.image = pygame.image.load(imagename)#图像
		self.rect = self.image.get_rect()#尺寸
		self.speed=speed

	def update(self):
		self.rect.y+=self.speed

class EnemySprite(GameSprite):#敌机子类
	def __init__(self):
		self.imagename='./images/enemy0.png'
		super().__init__(self.imagename)
		self.rect.bottom = 0#敌人随机初始化的位置
		maxvalue = SCREEN_RECT.width-self.rect.width#背景图的宽减去敌机的宽
		self.rect.x = random.randint(0,maxvalue)
		self.speed=random.randint(1,3)#敌机初始化速度


	def update(self):
		super().update()
		#判断是否移除屏幕
		if self.rect.top >= SCREEN_RECT.height:#敌机出屏幕
			self.kill()

class BackGroundSpriteadds(GameSprite):#背景精灵类
	def __init__(self,is_alt=False):
		self.imagename='./images/background.png'
		super().__init__(self.imagename,5)
		if is_alt:
			self.rect.y=-self.rect.height
	def update(self):
		super().update()
		if self.rect.top>=SCREEN_RECT.height:
			self.rect.y=-self.rect.height#背景更换
		
class Hero(GameSprite):
#"""英雄精灵"""
	def __init__(self):
		self.imagename = "./images/hero.gif"
		super().__init__(self.imagename,0)#0速度
		# 设置初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 50
		self.bullet_group = pygame.sprite.Group()
	def update(self):
		self.rect.x+=self.speed
		# 判断屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if  self.rect.right >= SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

		self.rect.y += self.speed1
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom		

	def fire(self):
			bullet = BulletSprite()
			bullet.rect.centerx = self.rect.centerx
			bullet.rect.y = self.rect.top - 20
			self.bullet_group.add(bullet)


			bullet1 = BulletSprite()
			bullet1.rect.centerx = self.rect.centerx - 35
			bullet1.rect.y = self.rect.top +35
			self.bullet_group.add(bullet1)

			bullet2 = BulletSprite()
			bullet2.rect.centerx = self.rect.centerx + 35
			bullet2.rect.y = self.rect.top + 35
			self.bullet_group.add(bullet2)
		
class BulletSprite(GameSprite):#子弹精灵
	def __init__(self):
		self.imagename = "./images/bullet1.png"	
		super().__init__(self.imagename,-20)
	
	def __del__(self):
		print("子弹销毁了")	

	def update(self):
		super().update()
		if self.rect.bottom <= 0:
			self.kill()	


	






	
