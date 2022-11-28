import pymysql
connection=pymysql.connect(host='localhost',
                   user='root',
                   password='admin',
                   database='demo2',
                   cursorclass=pymysql.cursors.DictCursor)

#cursor=db.cursor()
#cursor.execute("SELECT VERSION()")
#data=cursor.fetchone()

#print("Database -`version: %s " % data)
#query='INSERT INTO student VALUES ("JOHN","Dell",24,"0812CS141020")'
#try:
 #    cursor.execute(query)
  #   db.commit()
#except:
 #   db.rollback()
#db.close()
with connection.cursor() as cursor:
    sql="SELECT* FROM student"
    cursor.execute(sql)
    result=cursor.fetchone()
    print(result)


