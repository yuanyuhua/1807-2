class sushu():
	def guocheng(self):
		
		j = 2
		i = 2
		for i in range(2,101):
			flag = 1      #立个假设：(2,101)全是素数
			for j in range(2,i):  #验证
				if i%j == 0:
					flag = 0
					break
			if flag == 1:
				print(i)
ss = sushu()
ss.guocheng()
