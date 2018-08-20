import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
class GameSprite(pygame.sprite.Sprite): #父类
	def __init__(self,imagename,speed = 1):  #初始化  
		super().__init__()#调用父类方法
		self.image = pygame.image.load(imagename)#加载图像
		self.rect = self.image.get_rect()#获取图像的外面的长方形
		self.speed = speed
	def update(self):
		self.rect.y+=self.speed #相当速度


class EnemySprite(GameSprite):#敌机子类
	def __init__(self):
		self.imagename = "./images/enemy0.png" #传入图片路径
		super().__init__(self.imagename,10) #让父类帮忙加载
		if is_alt:
			self.rect.y =- self.rect.height

	def update(self): #更新
		super().update()#调父类
		if rece.top >= SCREEN_RECT.height:
			self.rect.y =- self.rect.height

class BackGroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		super().__init__(self.imagename)
	def update(self):
		super().update()
class Hero(GameSprite):
	def __init(self):
		super().__init__("./images/me1.png",0)
		self.rect.centrx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

		
