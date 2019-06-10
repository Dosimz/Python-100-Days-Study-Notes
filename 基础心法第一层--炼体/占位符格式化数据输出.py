"""
占位符格式化数据输出字符串

Version: 0.1
Author: 余漪
"""

a = int(input('a = '))
b = int(input('b = '))
# 格式化字符串里包含"%",必须用"%%"
print('%d %% %d = %d' % (a, b, a % b))