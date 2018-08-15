class car():
	def __init__(self,name,color):
		self.name = name
		self.__color = color#私有方法不被继承 
class falali(car):
	pass
class mashaladi(car):
	pass
f = falali("法拉利","红色")
print(f.name,f.color)
m = mashaladi("玛莎拉蒂","黑色")
print(m.name,m.color)
