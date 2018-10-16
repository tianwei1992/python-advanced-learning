# -*- coding: utf-8 -*
"""用lambda实现的嵌套，更自然"""
def func():
	x = 4
	action = (lambda n:x ** n)
	return action

x = func()
print(x(2))

"""以上得以运行是LEGB的E，但是对早期版本不适用。为了适用应该这样："""
def func():
	x = 4
	action = (lambda n, x =x:x ** n)
	return action

x = func()
print(x(2))

