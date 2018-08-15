class a():
	def a(self):
		import random
		a = random.randint(1,100)
		print("生成随机数为:%d"%a)
		i = 0
		while True:
			num = int(input("输入你猜的数字1-100:"))
			i += 1
			if a > num:
				print("输入错误,数太小了")
			elif a < num:
				print("输入错误,数太大了")
			elif a == num:
				print("输入正确")
				break
b = a()
b.a()

