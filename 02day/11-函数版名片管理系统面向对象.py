list = []
while True:
	def a():
		d = {}
		
		name = input("请输入姓名")
		age = int(input("请输入年龄"))
		d["name"] = name
		d["age"] = age
		list.append(d)
		w()


	def w():
		f = open("1.txt","w")
		f.write(str(list))
		f.close()
		r()


	def r():
		f1 = open("data.data","r")
		content = f1.read()
		if len(content) != 0:
			list = eval(content) #26+31 =print(content)	
			for i in list:
				for k,v in i.items():
					print(k,v)

			print(list)
		f1.close()
	a()	

