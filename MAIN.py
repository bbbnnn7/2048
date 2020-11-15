import random
li = []
ch1 = []
ch2 = []
scre = int(0)
for i in range(4):
	li.append([])
	for j in range(4):
		li[i].append(int(0))

for i in range(4):
	ch1.append(0)
	ch2.append(0)

print(li)
print(scre)
def rndm():
	lor = []
	for i in range(4):
		for j in range(4):
			if li[i][j] == 0:
				lor.append((i , j))
	rr = random.randrange(len(lor))
	rch = random.choices([2 , 4] , [8 , 1] , k=1)
	li[lor[rr][0]][lor[rr][1]] =  int(rch[0])

def gameover():
	lor = []
	for i in range(4):
		for j in range(4):
			if li[i][j] == 0:
				lor.append((i , j))
	try: rr = random.randrange(len(lor))
	except ValueError: 
		print("Game Over")
		quit()

def prnt():
	for i in range(4):
		for j in range(4):
			print(li[i][j] , end=' ')
		print()

def check():
	sh1 = []
	sh2 = []
	for i in range(4):
		ch01 = 0
		ch02 = 0
		for j in range(4):
			ch01 += li[i][j]
			ch02 += li[j][i]
		sh1.append(ch01)
		sh2.append(ch02)
	chck = 0
	for i in range(4):
		if sh1[i] == ch1[i] and sh2[i] == ch2[i]:
			chck += 1
	if chck != 4:
		rndm()
		sh1 = []
		sh2 = []
		for i in range(4):
			ch01 = 0
			ch02 = 0
			for j in range(4):
				ch01 += li[i][j]
				ch02 += li[j][i]
			sh1.append(ch01)
			sh2.append(ch02)
		for i in range(4):
			ch1[i] = sh1[i]
			ch2[i] = sh2[i]
		print(ch1 , ch2 , chck)
	if chck == 4:
		gameover()

def plsc(self):
	why = scre
	why += 2 * int(self)
	scre = why

def sad(do):
	if do == "h":
		for i in range(4):
			dc = []
			for j in range(4):
				if li[i][j] != 0:
					dc.append(li[i][j])
			l = len(dc)
			if l == 0:
				continue
			if l == 1:
				for j in range(4):
					if j < l:
						li[i][j] = dc[j]
					else:
						li[i][j] = 0
				continue	
			ji = 0
			while ji < len(dc)-1:
				if dc[ji] == dc[ji+1]:
					plsc(dc[ji])
					dc[ji] += dc[ji+1]
					del dc[ji+1]
				ji += 1
			l = len(dc)
			for j in range(4):
				if j < l:
					li[i][j] = dc[j]
				else:
					li[i][j] = 0
		check()

	elif do == "k":
		for i in range(4):
			dc = []
			for j in range(4):
				if li[j][i] != 0:
					dc.append(li[j][i])
			l = len(dc)
			if l == 0:
				continue
			if l == 1:
				for j in range(4):
					if j < l:
						li[j][i] = dc[j]
					else:
						li[j][i] = 0
				continue	
			ji = 0
			while ji < len(dc)-1:
				if dc[ji] == dc[ji+1]:
					plsc(dc[ji])
					dc[ji] += dc[ji+1]
					del dc[ji+1]
				ji += 1
			l = len(dc)
			for j in range(4):
				if j < l:
					li[j][i] = dc[j]
				else:
					li[j][i] = 0
		check()

	elif do == "j":
		for i in range(4):
			dc = []
			for j in range(4):
				if li[j][i] != 0:
					dc.append(li[j][i])
			l = len(dc)
			if l == 0:
				continue
			if l == 1:
				for j in range(4):
					if 4-j > l:
						li[j][i] = 0
					else:
						li[j][i] = dc[l-4+j]
				continue	
			ji = len(dc)-1
			while ji > 0:
				if dc[ji] == dc[ji-1]:
					plsc(dc[ji])
					dc[ji] += dc[ji-1]
					del dc[ji-1]
					ji -= 1
				ji -= 1
			l = len(dc)
			for j in range(4):
				if 4-j > l:
					li[j][i] = 0
				else:
					li[j][i] = dc[l+j-4]
		check()


	elif do == "l":
		for i in range(4):
			dc = []
			for j in range(4):
				if li[i][j] != 0:
					dc.append(li[i][j])
			l = len(dc)
			if l == 0:
				continue
			if l == 1:
				for j in range(4):
					if 4-j > l:
						li[i][j] = 0
					else:
						li[i][j] = dc[l-4+j]
				continue	
			ji = len(dc)-1
			while ji > 0:
				if dc[ji] == dc[ji-1]:
					plsc(dc[ji])
					dc[ji] += dc[ji-1]
					del dc[ji-1]
					ji -= 1
				ji -= 1
			l = len(dc)
			for j in range(4):
				if 4-j > l:
					li[i][j] = 0
				else:
					li[i][j] = dc[l-4+j]
		check()


	elif do == 'q':
		quit()
	

if __name__ == "__main__":
	rndm()
	while True:
		prnt()
		print(scre)
		inp = input()
		sad(inp)
