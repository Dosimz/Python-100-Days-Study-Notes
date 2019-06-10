import pymysql


def main():
    no = int(input('编号： '))
    name = input('名字： ')
    loc = input('所在地： ')
    # 1. 创建数据库链接
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='',
                          autocommit=True)
    try:
        # 2. 通过链接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'update tb_dept set dname=%s, dloc=%s where dno=%s',
                (name, loc, no)
            )
    finally:
        # 4. 关闭链接，释放资源
        con.close()