mport pygame
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,imagename,speed):
		super().__init__()
		self.image = pygame,image.load(imsgenmsnr)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):
		self.recr.y +=self.speed
class EnemySorinte(GameSprite):
	def __init__(self):
		self.imagename = "./images/enemy0.png"
		super().__init__(self,imagname)

	def update(self):
		super().update()
