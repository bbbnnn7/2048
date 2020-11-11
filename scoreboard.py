import pygame

class Scoreboard:
	def __init__(self , game):
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()
		self.color = (0 , 0 , 0)
		self.font = pygame.font.SysFont(None , 54)
		self.open_file = open('text')
		self.score = 0
		self.hs = int(self.open_file.readline())
		self.open_file.close()
		self.prep_score()
		self.prep_hs()
	
	def prep_score(self):
		score_str = str(self.score)
		self.image_score = self.font.render(score_str , True , self.color , (250 , 250 , 250))
		self.score_rect = self.image_score.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_hs(self):
		hs_str = str(self.hs)
		self.image_hs = self.font.render(hs_str , True , self.color , (250 , 250 , 250))
		self.hs_rect = self.image_hs.get_rect()
		self.hs_rect.left = self.screen_rect.left + 20
		self.hs_rect.top = 20
	
	def show_score(self):
		self.screen.blit(self.image_score , self.score_rect)
		self.screen.blit(self.image_hs , self.hs_rect)
