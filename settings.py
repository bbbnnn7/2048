import random

class Settings:
	def __init__(self):
		self.width = 800
		self.height = 900
		self.bg_color = (250 , 250 , 250)
		self.bb_color = (150  , 150 , 150)
		self.bb_width = 600
		self.bb_height = 600
		self.num_color = []
		self.change_color()

	def change_color(self):
		color = (0 , 0 , 0)
		for i in range(3):
			for j in range(5):
				neco = list(color)
				neco[i] += (j + 1) * 50
				neco = tuple(neco)
				self.num_color.append(neco)
		self.num_color[0] = (150 , 150 , 150)
		self.num_color.insert(0 , (200 , 200 , 200))
