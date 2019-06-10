import pymysql


def main():
    no = int(input('编号: '))
    # 1. 创建数据库链接
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='',
                          autocommit=True)
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'delete from tb_dept where dno=%s',
                (no, )
            )
        if result == 1:
            print('删除成功！')
    finally:
        # 4. 关闭链接，释放资源
        con.close()

if __name__ == "__main__":
    main()