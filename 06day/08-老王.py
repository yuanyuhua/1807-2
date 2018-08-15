class showerror(Exception):
	def __init__(self,name):
		self.name = name
class  error():
	def my_input(self):
		self.name = input("请输入名字")		
		try:
			if self.name == "老王":
				raise showerror(self.name)
		except showerror as ret:
			print("输入%s就报错"%ret.name)

show = error()
show.my_input()
