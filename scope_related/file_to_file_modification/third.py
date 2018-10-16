"""second.py导入了first.py并直接对其中的比那辆进行了赋值，然后在本模块third.py中另外导入first.py，观察中的变量值是否受到了影响"""
import second
"""说明second的执行已经改变了first.py文件中的变量值了！可怕！"""
import first
print(first.X)

"""输出：
99
66"""
""""""

