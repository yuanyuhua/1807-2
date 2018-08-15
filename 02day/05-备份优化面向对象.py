class beifen():
	def beifen(self):
		name = input("请输入备份的名称")
		f = open(name,"r")
		content = f.read()

		position = name.rfind(".")
		newname = name[:position] + "备份" + name[position:]

		f1 = open(newname,"w")
		while True:
			content = f.read(1024)
			f1.write(content)
			if len(content) == 0:
				break	

		f.close()
		f1.close()
bf = beifen()
bf.beifen()






name = input("请输入你要备份的文件的文件名")
f = open(name,"r")
content = f.read()
position = name.rfind(".")
newname = name[:position] + "备份" + neme[position:]
f1 = open(name,"w")
while True:
	content = f.read(1024)
	f1.write(content)
	if len(content) == 0:
		break
f.close()
f1.close()































