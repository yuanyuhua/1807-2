money = 0
d = float(input("请输入距离"))
for i in range(1,31):
	print("%d天"%i)
	for i in range(1,3):#一天做两次
		print("%d"%j)
		if d <= 6:
			p = 3
		elif d > 6 and d <= 12:
			p = 4
		elif d > 12 and d <= 22:
			p = 5
		elif d > 22 and d <= 32:
			p = 6
		elif d > 32:
			if (d - 32)%20 == 0:
				p = 6 + (d -32)/20
			elif (d - 32)%20 != 0:
				p = 6 + int((d - 32)/20)+1
		if money > 100 and money <=150:
			p = p*0.8
		elif money > 150 and money <= 400:
			p = p*0.5
		money = money + p


