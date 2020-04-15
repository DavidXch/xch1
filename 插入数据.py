import pymysql

id='519030910082'
user='xch'
age=19

db=pymysql.connect(host='localhost',user='root',password='Xch1017lxl',port=3306,db='spiders')
cursor=db.cursor()
sql='INSERT INTO students(id,name,age) valuess(%s,%s,%s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()