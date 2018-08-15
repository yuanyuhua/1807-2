class jiecheng():
	def jiecheng(self):
		def a(num):
			if num == 1:
				return 1
			elif num != 1:
				return num*a(num-1)
		b = a(5)
		print(b)
jc = jiecheng()
jc.jiecheng()
