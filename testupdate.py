import pymysql
from pymsgbox import password

connection = pymysql.connect(host ='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
sql = "update marksheet set name = 'ram' where id = 4"
cursor.execute(sql)
connection.commit()
connection.close()
print("data inserted")