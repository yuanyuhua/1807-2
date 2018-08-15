class chuquan():
	def chuquan(self):
		import random
		cp = random.randint(1,3)
		player = input("请输入 1、石头，2、剪刀，3、布")
		if cp == 1 and player == 2 or cp == 2 and player == 3 or cp == 3 and player == 1:
			print("电脑赢")
		elif cp == player:
			print("平局")
		else:
			print("玩家赢")

cq = chuquan()
cq.chuquan()
