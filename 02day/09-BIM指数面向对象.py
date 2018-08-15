class a():
	def a(self):
		height = float(input("请输入身高:"))
		weight = float(input("请输入体重:"))
		BIM = weight/height*height
		if BIM < 18.5:
			print("过轻")
		elif BIM >= 18.5 and BIM < 25: 
			print("正常")
		elif BIM >= 25 and BIM < 28:
			print("过重")
		elif BIM >= 28 and BIM <= 32:
			print("肥胖")
		elif BIM > 32:
			print("严重肥胖")
b = a()
b.a()

