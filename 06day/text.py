def jisuanqi(a,b,x):
	if x == "+":
		return a+b
	elif x == "-":
		return a-b
	elif x == "*":
		return a*b
	elif x == "/":
		if b != 0:		
			return a/b
		else:
			print("输入有误") 
	
