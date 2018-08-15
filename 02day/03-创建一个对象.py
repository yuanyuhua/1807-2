class Car:
	#有行为的类
	def run(self):
		print("跑")
	def turn(self):
		print("转向")


mashaladi = Car()#通过汽车类创建出一个mashaladi的对象
mashaladi.run()#目前不需要传参数
mashaladi.turn()#目前不需要传参数



class Bingxiang():
	def opendoor(self):
			print("开门")
	def zhuangdaxiang(self):
			print("装大象")
	def closedoor(self):
			print("关门")	

geli = Bingxiang()
geli.opendoor()
geli.zhuangdaxiang()
geli.closedoor()







class person():
	def shenghaizi(self):
		print("生孩子")
	def eat(self):
		print("吃饭")
	def sleep(self):
		print("睡觉")
women = person()
women.shenghaizi()
women.eat()
women.sleep()
