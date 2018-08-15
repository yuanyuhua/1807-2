class dog():
	def __init__(self):
		self.name = "二哈"
	def __str__(self):
		print("哈哈哈哈")
	def __del__(self):
		print("呵呵")
Dog = dog()
#dog1 = dog
Dog1 = dog()
del dog
print("哦哦")
