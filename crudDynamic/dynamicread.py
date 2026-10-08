import pymysql

# def testread1():
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='rays')
#     cursor = connection.cursor()
#     sql = "select * from marksheet"
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     for row in data:
#         print(row)
#     connection.commit()
#     connection.close()
#print("data Read Successfully")

def testread2():
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        sql = "select * from marksheet"
        cursor.execute(sql)
        data = cursor.fetchall()
        columnName = ('id','rollNo', 'name','phy','chm','maths')
        for x in data:
            print(x)
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.commit()
        connection.close()
