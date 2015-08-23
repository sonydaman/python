#!C:/Python27/python.exe

#print "Set-Cookie:UserID=XYZ;\r\n"
#print "Set-Cookie:Password=XYZ123;\r\n"
#print "Set-Cookie:Expires=Tuesday, 31-Dec-2007 23:12:40 GMT";\r\n"
#print "Set-Cookie:Domain=http://localhost:8089/;\r\n"
#print "Set-Cookie:Path=cookie;\n"

# Import modules for CGI handling 

import cgi, os, cgitb 
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
fileitem = form['filename']
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open('tmp/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'


# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
if form.getvalue('maths'):
   math_flag = "ON"
else:
   math_flag = "OFF"

if form.getvalue('physics'):
   physics_flag = "ON"
else:
   physics_flag = "OFF"
if form.getvalue('textcontent'):
   text_content = form.getvalue('textcontent')
else:
   text_content = "Not entered"
if form.getvalue('dropdown'):
   subject = form.getvalue('dropdown')
else:
   subject = "Not entered"  
   
   
   
   
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s</h2>" % (first_name, last_name)
print "<h2> CheckBox Maths is : %s</h2>" % math_flag
print "<h2> CheckBox Physics is : %s</h2>" % physics_flag
print "<h2> Entered Text Content is %s</h2>" % text_content
print "<h2> Selected Subject is %s</h2>" % subject
print "<h2> Selected Subject is %s</h2>" % message
print "</body>"
print "</html>"