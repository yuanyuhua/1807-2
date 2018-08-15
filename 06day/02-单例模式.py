class dog():
	__instance = None  #引用
	__flag = False
	def  __init__(self,name):
		if son.__flag == False:
			self.name = name
			son.__self = True

	def __new__(clas,*args,**kwargs):
		if clas. __instance == None:
			clas.__instance = super().__new__(clas)
			return clas.__instance
		else:
			return clas. __instance
Dog = dog()
print(id(Dog))

Dog1 = dog
print(id(Dog))
		
print(Dog.name)
print(id(Dog))
