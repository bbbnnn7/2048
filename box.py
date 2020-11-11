import pygame

from pygame.sprite import Sprite
from settings import Settings

class Bigbox:
	def __init__(self , game):
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		self.set = game.set
		self.color = self.set.bb_color
		self.rect = pygame.Rect(0 , 0 ,self.set.bb_width , self.set.bb_height)
		self.rect.center = self.screen_rect.center

	def drawbb(self):
		pygame.draw.rect(self.screen , self.color , self.rect)

class Box(Sprite):
	def __init__(self , bb):
		super().__init__()
		self.screen = bb.screen
		self.width = 140
		self.color = (200 , 200 , 200)
		self.set = Settings()
		self.rect = pygame.Rect(0 , 0 , self.width , self.width)

	def draw_box(self , num):
		pygame.draw.rect(self.screen , self.set.num_color[num] , self.rect)
