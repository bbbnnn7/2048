import pygame
import sys

from settings import Settings
from box import Bigbox
from box import Box
from main import Main
from print import Print
from scoreboard import Scoreboard

class Game:
	def __init__(self):
		pygame.init()
		self.set = Settings()
		self.screen = pygame.display.set_mode((self.set.width , self.set.height))
		pygame.display.set_caption("Game2048")
		self.bb = Bigbox(self)
		self.box = pygame.sprite.Group()
		self.main = Main()
		self._print = Print(self)
		self.sb = Scoreboard(self)
		self._create_box()

	def _create_box(self):
		box = Box(self.bb)
		size = box.width
		available_space = self.set.bb_width - 16
		number_a = available_space // size
		num = 0
		for row_number in range(number_a):
			for box_number in range(number_a):
				new = Box(self)
				new.rect.x = 8 + 8 * box_number + box_number * new.width + self.bb.rect.x
				new.rect.y = 8 + 8 * row_number + row_number * new.width + self.bb.rect.y
				self._print.prep_num(new , self.main.li[row_number][box_number] , num , 0)
				self.box.add(new)
				num += 1
	
	def _check_box(self):
		num = 0
		row_number = 0
		box_number = 0
		for box in self.box.sprites():
			ex = 0 
			exn = 1
			for i in range(15):
				if exn == self.main.li[row_number][box_number] or 0 == self.main.li[row_number][box_number]:
					break
				exn *= 2
				ex += 1
			box.draw_box(ex)
			self._print.prep_num(box , self.main.li[row_number][box_number] , num , ex)
			num += 1
			row_number = num // 4
			box_number = num % 4

	def _check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown(event)
#			elif event.type == pygame.KEYUP:
#				self._check_keyup(event)

	def _check_keydown(self , event):
		if event.key == pygame.K_q:
			sys.exit()
		else:
			self.main.sad(event.key)
			self._check_score()

#	def _check_keyup(self , event):
		

	def _check_score(self):
		self.sb.score = self.main.sc
		self.sb.prep_score()
		
	def _check_hs(self):
		if self.sb.score > self.sb.hs:
			self.sb.hs = self.sb.score
			self.open_file = open('text' , 'w')
			self.open_file.write(str(self.sb.hs))
			self.open_file.close()
			self.sb.prep_hs()

	def _screen_update(self):
		num = 0
		self.screen.fill(self.set.bg_color)
		self.bb.drawbb()
		for box in self.box.sprites():
			box.draw_box(num)
		self._check_box()
		for i in range(16):
			num_row = i % 4
			num_col = i // 4
			if self.main.li[num_col][num_row] == 0:
				continue
			self._print.prnt(i)
		self.sb.show_score()
		pygame.display.flip()

	def run(self):
		while True:
			self._check_event()
			self._check_hs()
			self._screen_update()
	

if __name__ == '__main__':
	game = Game()
	game.run()


