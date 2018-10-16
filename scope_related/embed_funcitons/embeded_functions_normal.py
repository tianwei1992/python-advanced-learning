# -*- coding: utf-8 -*
"""LEGB中的E"""
def maker(N):
	def action(X):
		return X ** N
	return action

f = maker(2)
print(f(8))
print(f(3))

g = maker(3)
print(g(6))
print()

"""但以上在py2不好用，py2没有E的概念，必须要用默认参数传进去"""
def maker(N):
	def action(X, N = N):# 默认参数
		return X ** N
	return action

f = maker(2)
print(f(8))
print(f(3))

g = maker(3)
print(g(6))
print()

