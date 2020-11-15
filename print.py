import pygame

from settings import Settings

class Print:
	def __init__(self , game):
		self.screen = game.screen
		self.set = Settings()
		self.font = pygame.font.SysFont(None , 48)
		self.ncolor = (0 , 0 , 0)
		self.num_image = {}
		self.num_rect = {}
	
	def prep_num(self , box , li , num , ex):
		num_str = str(li)
		self.num_image[num] = self.font.render(num_str , True , (0 , 0 , 0) , self.set.num_color[ex])
		self.num_rect[num] = self.num_image[num].get_rect()
		self.num_rect[num].center = box.rect.center

	def prnt(self , num):
		self.screen.blit(self.num_image[num] , self.num_rect[num])
