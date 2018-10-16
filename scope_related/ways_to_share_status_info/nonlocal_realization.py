def tester(start):
	state = start
	def nested(label):
		nonlocal state
		print(label, state)
		state += 1    #没有nolocal是不能修改E作用域中变量的
	return nested

F = tester(0)
F("spam")
F("ham")
F("eggs")


K = tester(100)
K("spam")
K("ham")
K("eggs")

F("spam")
F("ham")
F("eggs")

"""F的3次执行，每次执行都共享（操作）到F里的公有变量（状态）。K也是同理。但这个状态只在F内部，不会与其他函数冲突，F和K也是相互隔离的

这时的F和G非常类似于同一个类的两个实例，彼此从同一个模式派生出来（不管是从类还是一个嵌套的上层函数，实例对象的多次执行可能会操作到共同的状态变量，但两个实例之间又完全是不同的作用域"""

"""python2不支持nonlocal，可以用global等效实现：
只能靠定义一个全局变量，然后在f1和f2的作用域里分别global声明这个全局变量
-》这是有效的，但是tester(0)和test(1）就会扯在一起,互相干扰。
"""