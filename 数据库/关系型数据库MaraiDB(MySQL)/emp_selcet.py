import pymysql
from pymysql.cursors import DictCursor

class Emp(object):
    
    def __init__(self, no, name, job, sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位:{self.job}\n月薪：{self.sal}\n'

def main():
    page = int(input('页码： '))
    size = int(input('大小： '))
    con = pymysql.connect(host='localhost',port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='')
    try:
        with con.cursor() as cursor:
            cursor.execute(
                'select eno as no, ename as name, job, sal from tb_emp limit %s, %s',
                ((page - 1) * size, size)
            )
            for emp_tuple in cursor.fetchall():
                emp = Emp(*emp_tuple)
                print(emp)
    finally:
        con.close()

if __name__ == "__main__":
    main()