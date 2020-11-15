import random

class Settings:
	def __init__(self):
		self.width = 800
		self.height = 900
		self.bg_color = (200 , 250 , 250)
		self.bb_color = (204 , 192  , 179)
		self.bb_width = 600
		self.bb_height = 600
		self.num_color = []
		self.change_color()

	def change_color(self):
		self.num_color.append((238 , 228 , 218))
		self.num_color.append((237 , 224 , 200))
		self.num_color.append((242 , 177 , 121))
		self.num_color.append((245 , 149 , 99))
		self.num_color.append((246 , 124 , 95))
		self.num_color.append((246 , 94 , 59))
		self.num_color.append((237 , 207 , 114))
		self.num_color.append((237 , 204 , 97))
		self.num_color.append((237 , 200 , 80))
		self.num_color.append((237 , 197 , 63))
		self.num_color.append((237 , 194 , 46))
		self.num_color.append((0 , 0 , 0))
		self.num_color.append((0 , 0 , 0))
		self.num_color.append((0 , 0 , 0))
		self.num_color.append((0 , 0 , 0))
		self.num_color.append((0 , 0 , 0))
		self.num_color.append((0 , 0 , 0))
		print(self.num_color)
