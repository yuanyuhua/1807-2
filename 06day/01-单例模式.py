class Dog():
	__instance = None
	__flag = False
	def __init__(self,name):
		if Dog.__flag == False:
			self.name = name
			Dog.__flag = True

	def __new__(clas,*args,**kwargs):
		if clas.__instance == None:
			clas.__instance = super().__new__(clas)
			return clas.__instance
		else:
			return clas.__instance

dog = Dog("小红")
print(id(dog))
dog1 = Dog("小明")
print(id(dog1))

print(dog.name)
print(dog1.name)
			
		 
