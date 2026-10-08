import pymysql

from PDBC.testupdate import connection


# def testinsert():
#     connection = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password='root',database = 'rays')
#     cursor = connection.cursor()
#     sql= "insert into marksheet values(25,66,'shyam',41,21,01)"
#     cursor.execute(sql)
#     connection.commit()
#     connection.close()
#     print("data inserted")

# def testinsert2():
#     connection = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password='root',database = 'rays')
#     cursor = connection.cursor()
#     sql= "insert into marksheet values(%s,%s,%s,%s,%s,%s)"
#     data = (30,171,'XYZ',45,78,12)
#     cursor.execute(sql,data)
#     connection.commit()
#     connection.close()
#     print("data inserted")


def insert3(id, rollNo, name, phy, chm, maths):
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='rays'
    )

    cursor = connection.cursor()

    sql = "INSERT INTO marksheet VALUES(%s, %s, %s, %s, %s, %s)"

    data = (id, rollNo, name, phy, chm, maths)

    cursor.execute(sql, data)

    connection.commit()
    connection.close()

    print('data inserted3 successfully')


insert3(35, 1033, 'Tanishq', 80, 75, 90)


# def dynamicinsert(data={}):
#     id = data['id']
#     rollNo = data['rollNo']
#     name = data['name']
#     phy = data['phy']
#     chm = data['chm']
#     maths = data['maths']
#     connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='rays')
#     cursor = connection.cursor()
#     sql = "insert into marksheet values(%s, %s, %s, %s,%s,%s)"
#     data = (id, rollNo,name, phy,chm,maths)
#     cursor.execute(sql, data)
#     connection.commit()
#     connection.close()
#     print('data inserted4 successfully')

#testinsert3(33,118,"ram",25,60,60)
