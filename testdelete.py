import pymysql
from pymsgbox import password

connection = pymysql.connect(host ='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
sql = "delete from marksheet where id = 5"
cursor.execute(sql)
connection.commit()
connection.close()
print("data inserted")