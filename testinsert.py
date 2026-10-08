import pymysql
from pymsgbox import password

connection = pymysql.connect(host ='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
sql = "insert into marksheet values(17,132,'om',54,78,65)"
cursor.execute(sql)
connection.commit()
connection.close()
print("data inserted")