import pygame
pygame.init()
yh = pygame.Rect(480,300,120,120)
screen = pygame.display.set_mode((480,700))
ba = pygame.image.load("./images/background.png")
screen.blit(ba,(0,0))
pygame.display.update()
while True:
	pass
pygame.quit()
