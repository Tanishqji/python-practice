import pymysql
from pymsgbox import password
connection = pymysql.connect(host ='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
sql = "select  * from  marksheet"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
     print(data[0],data[1],data[2],data[3])
connection.commit()
connection.close()
print("data inserted")