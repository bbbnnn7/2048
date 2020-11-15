import random
import pygame
import time
	
class Main:
	def __init__(self):
		self.li = []
		self.ch1 = []
		self.ch2 = []
		for i in range(4):
			self.li.append([])
			for j in range(4):
				self.li[i].append(int(0))

		for i in range(4):
			self.ch1.append(0)
			self.ch2.append(0)
		self.sc = 0
		self.rndm()
            
	def rndm(self):
		lor = []    
		for i in range(4):
			for j in range(4):
				if self.li[i][j] == 0:
					lor.append((i , j))
		rr = random.randrange(len(lor))
		rch = random.choices([2 , 4] , [8 , 1] , k=1)
		self.li[lor[rr][0]][lor[rr][1]] =  int(rch[0])

	def check(self):
		sh1 = []
		sh2 = []
		for i in range(4):
			ch01 = 0
			ch02 = 0
			for j in range(4):
				ch01 += self.li[i][j]
				ch02 += self.li[j][i]
			sh1.append(ch01)
			sh2.append(ch02)
		chck = 0
		for i in range(4):
			if sh1[i] == self.ch1[i] and sh2[i] == self.ch2[i]:
				chck += 1
		if chck != 4:
			self.rndm()
			sh1 = []
			sh2 = []
			for i in range(4):
				ch01 = 0
				ch02 = 0
				for j in range(4):
					ch01 += self.li[i][j]
					ch02 += self.li[j][i]
				sh1.append(ch01)
				sh2.append(ch02)
			for i in range(4):
				self.ch1[i] = sh1[i]
				self.ch2[i] = sh2[i]

	def sad(self , do):
		bl = True
		if do == pygame.K_LEFT and bl:
			for i in range(4):
				dc = []
				for j in range(4):
					if self.li[i][j] != 0:
						dc.append(self.li[i][j])
				l = len(dc)
				if l == 0:
					continue
				if l == 1:
					for j in range(4):
						if j < l:
							self.li[i][j] = dc[j]
						else:
							self.li[i][j] = 0
					continue	
				ji = 0
				while ji < len(dc)-1:
					if dc[ji] == dc[ji+1]:
						dc[ji] += dc[ji+1]
						self.sc += dc[ji]
						del dc[ji+1]
					ji += 1
				l = len(dc)
				for j in range(4):
					if j < l:
						self.li[i][j] = dc[j]
					else:
						self.li[i][j] = 0
			self.check()
			bl = False

		elif do == pygame.K_UP and bl:
			for i in range(4):
				dc = []
				for j in range(4):
					if self.li[j][i] != 0:
						dc.append(self.li[j][i])
				l = len(dc)
				if l == 0:
                        		continue
				if l == 1:
                        		for j in range(4):
                            			if j < l:
                                			self.li[j][i] = dc[j]
                            			else:
                                			self.li[j][i] = 0
                        		continue	
				ji = 0
				while ji < len(dc)-1:
                        		if dc[ji] == dc[ji+1]:
                            			dc[ji] += dc[ji+1]
                            			self.sc += dc[ji]
                            			del dc[ji+1]
                        		ji += 1
				l = len(dc)
				for j in range(4):
                        		if j < l:
                            			self.li[j][i] = dc[j]
                        		else:
                            			self.li[j][i] = 0
			self.check()
			bl = False

		elif do == pygame.K_DOWN and bl:
			for i in range(4):
				dc = []
				for j in range(4):
					if self.li[j][i] != 0:
						dc.append(self.li[j][i])
				l = len(dc)
				if l == 0:
					continue
				if l == 1:
                       			for j in range(4):
                            			if 4-j > l:
                               		 		self.li[j][i] = 0
                            			else:
                                			self.li[j][i] = dc[l-4+j]
                        		continue	
				ji = len(dc)-1
				while ji > 0:
					if dc[ji] == dc[ji-1]:
						dc[ji] += dc[ji-1]
						self.sc += dc[ji]
						del dc[ji-1]
						ji -= 1
					ji -= 1
				l = len(dc)
				for j in range(4):
					if 4-j > l:
						self.li[j][i] = 0
					else:
						self.li[j][i] = dc[l+j-4]
			self.check()
			bl = False
                

		elif do == pygame.K_RIGHT and bl:
			for i in range(4):
				dc = []
				for j in range(4):
					if self.li[i][j] != 0:
						dc.append(self.li[i][j])
				l = len(dc)
				if l == 0:
					continue
				if l == 1:
					for j in range(4):
						if 4-j > l:
							self.li[i][j] = 0
						else:
							self.li[i][j] = dc[l-4+j]
					continue	
				ji = len(dc)-1
				while ji > 0:
					if dc[ji] == dc[ji-1]:
						dc[ji] += dc[ji-1]
						self.sc += dc[ji]
						del dc[ji-1]
						ji -= 1
					ji -= 1
				l = len(dc)
				for j in range(4):
					if 4-j > l:
						self.li[i][j] = 0
					else:
						self.li[i][j] = dc[l-4+j]
			self.check()
			bl = False
