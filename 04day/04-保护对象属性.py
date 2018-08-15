class dog():
	def __init__(self):
		self.name = "二哈"
		self.age = 0
	def sleep(self):
		print("睡觉")
	def setage(self,age):
		if age > 15 or age < 1:
			print("年龄不符合")
		else:
			self.age = age
	def getage(self):
		return self.age
d = dog()
d.setage(100)

print(d.age)
