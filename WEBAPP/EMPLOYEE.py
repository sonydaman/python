#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import MySQLdb

# Open database connection
db = MySQLdb.connect("127.0.0.1","root","","angularcode_megamenu" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM categories WHERE id  > '%d'" % (10)
try:
   
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall();
   
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print "id=%d, category=%d, description=%s, parent=%d <br/><br/>" % \
             (fname, lname, age, sex )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()