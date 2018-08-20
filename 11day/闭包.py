def line_conf(a,b):
	def line(x):
		return a*x+b
	return line

#y = 2x+3
line = line_conf(2,3)#a,b的值
print(line(5))#x的值
print(line(6))
print(line(7))
------------------------------
def line1(a,b,x):
	return a*x+b
line1(2,3,5)#a,b,x的值
line1(2,3,6)
