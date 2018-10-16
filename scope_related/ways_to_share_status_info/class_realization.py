class tester:
	def __init__(self, start):
		self.state = start
	def nested(self, label):
		print(label, self.state)
		self.state += 1

F = tester(0)
F.nested("spam")
F.nested("ham")

G = tester(100)
G.nested("toast")

F.nested("bacon")