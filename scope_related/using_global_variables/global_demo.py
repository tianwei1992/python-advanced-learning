# X = 88
def func():
	global X    #X可以提前存在，也可以不存在
	X = 99

func()
print(X)