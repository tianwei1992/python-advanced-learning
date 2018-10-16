def tester(state):
	def nested(label):
		nonlocal state
		print(label, state)
		state += 1    #没有nolocal就不能修改E作用域中的变量state
	return nested

F = tester(0)
F("spam")
F("ham")
F("eggs")
print()

def tester(state):
	def nested(label):
		# nonlocal state
		print(label, state)
		state.append(100)  # append操作不算修改，算引用
		# state += 1    #没有nolocal就不能修改E作用域中的变量state
	return nested

F = tester([1])
F("spam")
F("ham")
F("eggs")
