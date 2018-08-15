class dog():
	def __init__(self):
		self.name = "二哈"
		self.__age = 0
	def sleep(self):
		print("睡觉")

	def setage(self,age):
		if age < 1 or age > 15:
			print("年龄不符合")
		else:
			self.__age = age
	def getage(self):
		return self.__age

Dog = dog()

Dog.setage(19)#随便输入
print(Dog.getage())
