def tester(start):
	def nested(label):
		print(label, nested.state)
		nested.state += 1
	nested.state = start
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

""""这个比较巧妙，state变量干脆直接绑定在nested身上，其实和nonlocal的实现非常相像。当然这里讨巧一把后就可以节约nonlocal了"""