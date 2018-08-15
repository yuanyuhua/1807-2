class car():
	#作用：初始化属性
	def __init__(self,color,types):  #实例化方法 默认被调用
		self.color = color
		self.types = types
	def __str__(self):#相当于自我介绍
			msg = "我的颜色是%s,我的型号是%s"%(self.color,self.types)
			return msg
	def move(self):
		print("移动")
	def music(self):
		print("听音乐")
	
		

l = car("红色","法拉利")    #创建对象
l.move()
l.music()

print(l)
