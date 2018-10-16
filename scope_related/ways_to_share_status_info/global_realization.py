def tester(start):
	global state
	state = start
	def nested(label):
		global state
		print(label, state)
		state += 1
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
"""但这个共享范围太大，K和F完全打通了，相互影响"""