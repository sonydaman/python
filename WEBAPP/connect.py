#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import MySQLdb

# Open database connection
try:
	db = MySQLdb.connect("127.0.0.1","root","","angularcode_megamenu" )
	cursor = db.cursor()
	
	try:
	  sql = "INSERT INTO categories(id, \
       category, description, parent) \
       VALUES ('%d', '%d', '%s', '%d' )" % \
       (258, 150, "RaMu", 22)		
		# Execute the SQL command
	  cursor.execute(sql)
	   # Commit your changes in the database
	  db.commit()
	  print "Insterted Successfully"
	except:
	   # Rollback in case there is any error
	   db.rollback()
	   print "Some Error Occuered"
	
	cursor.execute("SELECT VERSION()")
	
	# Fetch a single row using fetchone() method.
	data = cursor.fetchone()

	print "Database version : %s " % data

	# disconnect from server
	db.close()
except:
	print "som"
# prepare a cursor object using cursor() method
