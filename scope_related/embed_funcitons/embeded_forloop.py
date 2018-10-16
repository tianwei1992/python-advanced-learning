"""当被嵌套的不是普通函数而是一个for循环时，必须默认参数把E的上一层函数的值传进去。否则，根据规则，内层的变量是在调用时查找，那时for循环已经倒尽头，每一轮循环中的变量值都是一模一样的"""
def makeActions():
	acts = []
	for i in range(5):
		acts.append(lambda x, i=i: i ** x) #lambda里面没有return
	return acts

acts = makeActions()
print(acts[1](3))
print(acts[2](3))
print(acts[3](3))
