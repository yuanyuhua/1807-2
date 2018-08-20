import pygame
from jinglingzu import *
pygame.init() #初始化

yh = pygame.Rect(480,300,120,120)
screen = pygame.display.set_mode((480,700))#创建游戏窗口，宽度和高度

bg = pygame.image.load("./images/background.png")#插入背景
hero = pygame.image.load("./images/hero1.png")#插入英雄
#screen.blit(hero,(200,500))#英雄的位置  

herorect = pygame.Rect(200,500,120,120)#把不规则的飞机圈到规则的长方形中

clock = pygame.time.Clock()#while true太快，创建时间钟

enemy = EnemySprite()#创建敌机精灵
enemy1 = EnemySprite()#创建敌机精灵
enemy1.rect.x = 50  #往右边靠点，避免飞机撞在一起
enemy1.rect.y = 700  
enemy1.speed = -2  #速度不同
enemy_group = pygame.sprite.Group(enemy,enemy1)#把精灵加到精灵组

while True:  #游戏循环
	clock.tick(60)#一秒刷新60次

	herorect.y -= 10#飞机往上走

	screen.blit(bg,(0,0))  #先绘制背景
	screen.blit(hero,herorect)  #再绘制飞机

	if herorect.bottom <= 0:#飞机飞出去了
		herorect.top = 700#y轴为700，控制飞机返航
		
	enemy_group.update()  #精灵组更新
	enemy_group.draw(screen)  #画到哪
	
	#事件监听
	for event in pygame.event.get():

		# 判断用户是否点击了关闭按钮
		if event.type == pygame.QUIT:
			print("退出游戏...")
			pygame.quit()

			# 直接退出系统
			#exit()

	pygame.display.update()#更新
	

