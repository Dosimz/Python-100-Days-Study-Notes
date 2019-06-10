"""
打印三角形图案
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Date: 2019-4-25 1: 20
"""

row = int(input('请输入打印星的行数'))
for i in range(row):
    # print('*' * (i + 1), end = '/n') end 默认为'/n'
    print('*' * (i + 1))

for i in range(row):
    print(' ' * (row - i - 1) + '*' * (i + 1))

for i in range(row):
    print(' ' * (row - i - 1)  + '*' * (2 * i + 1))