import MySQLdb
db = MySQLdb.connect("localhost","root","wbhzsl","Student" )
cursor = db.cursor()
cursor.execute("select * from student")
data = cursor.fetchone()
print data
db.close()