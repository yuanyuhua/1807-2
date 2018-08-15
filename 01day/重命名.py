import os
dir = input("请输入批量重命名的文件夹名称")
files = os.listdir(dir)
os.chdir(dir)       #切换到游戏的文件夹中
print(os.getcwd())   #查看当前目录的路径
for i in files:
	position = i.rfind(".")
	newname = i[:position] + "-腾讯" + i[position:]
	os.rename(i,newname)
