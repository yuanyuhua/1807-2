class phone():
	count = 0
	def __init__(self,color):
		self.color = color
		phone.count += 1 
	def call(self):
		print("打电话")

xiaomi = phone("红色")
xiaomi1 = phone("黑色")
print(phone.count)
