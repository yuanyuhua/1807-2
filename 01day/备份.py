



name = input("请输入备份的名称")

f = open(name,"r")
content = f.read()

position = name.rfind(".")
newname = name[:position] + "备份" + name[position:]




f1 = open("newname","w")
f1.write(content)
f.close()
f1.close()

