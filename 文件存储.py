import csv
import pymysql

db=pymysql.connect(host='localhost',user='root',password='Xch1017lxl',port=3306,charset='utf8')
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data=cursor.fetchone()
print('Database version:',data)
cursor.execute("CREATE DATABASE spiderstest1 DEFAULT CHARACTER SET utf8")
db.close