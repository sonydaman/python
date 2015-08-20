print "Hello, Python!"
if True:
    print "True"
else:
  print "False"




#-----------------------------------------------

                #SECOND PROGRAM

#-----------------------------------------------



  




# ---------------------------------------------------
                #THIRD PROGRAM
print ("------------------------------------------------------")
print("\t\tTHIRD PROGRAM")
print ("------------------------------------------------------")

#----------------------------------------------------


total = "ITEM ONE" + \
        "ITEM TWO" + \
        "ITEM THREE"
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
word        =   'word'
sentence    =   "This is a sentence."
a, b, c = 1, 2, "john" #this work on 3.4



try:
    #2.7
    print (" 2.7 \n " +total + paragraph + paragraph + word +sentence +'\n');
    print paragraph[2:5]  +'\n'    # Prints characters starting from 3rd to 5th
    print paragraph[2:]   +'\n'   # Prints string starting from 3rd character
    print paragraph * 2   +'\n'    # Prints string two times
    print paragraph + "TEST" # Prints concatenated string

except:
    #3.4
    print (" 3.4 \n ",total , paragraph , paragraph , word , sentence , a , b , c);

    
# ---------------------------------------------------
                #FOURTH PROGRAM
                #Waiting for the User
print ("------------------------------------------------------")
print("\t\tFOURTH PROGRAM")
print("\t\tWaiting for the User")
print ("------------------------------------------------------")

#----------------------------------------------------



s = raw_input("\n\nPress the enter key to exit.")
print("Received input is : ",s);

#Enter your input: [x*5 for x in range(2,10,2)]
#str = input("Enter your input: ");
#print "Received input is : ", str



# ---------------------------------------------------
                #FIFTH PROGRAM
                #import sys;

print ("------------------------------------------------------")
print("\t\t#FIFTH PROGRAM")
print("\t\timport sys")
print ("------------------------------------------------------")

#----------------------------------------------------



import sys;
x = 'foo';
sys.stdout.write(x + '\n')




# ---------------------------------------------------
                #SIXTH PROGRAM
                #sys.argv;

print ("------------------------------------------------------")
print("\t\t#SIXTH PROGRAM")
print("\t\tsys.argv")
print ("------------------------------------------------------")

#----------------------------------------------------



import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)








# ---------------------------------------------------
                #7th PROGRAM
                #WORKING WITH ARRAY[],Tuples()  CANNOT UPDATED  read-only lists;

print ("------------------------------------------------------\n")
print("\t\t#7th PROGRAM\n")
print("\t\tWORKING WITH ARRAY\n")
print ("------------------------------------------------------\n")

#----------------------------------------------------




list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists





# ---------------------------------------------------
                #8th PROGRAM
                #WORKING WITH Dictionary(OBJECT);

print ("------------------------------------------------------\n")
print("\t\t#8th PROGRAM\n")
print("\t\tWORKING WITH  Dictionary(OBJECT)\n")
print ("------------------------------------------------------\n")

#----------------------------------------------------




dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values




# ---------------------------------------------------
                #9th PROGRAM
                #WORKING WITH Dictionary(OBJECT);

print ("------------------------------------------------------\n")
print("\t\t#9th PROGRAM\n")
print("\t\tWORKING WITH  Getting current time\n")
print ("------------------------------------------------------\n")

#----------------------------------------------------


import time;

localtime = time.localtime(time.time())
print "Local current time :", localtime
print ("------------------------------------------------------\n")
#Getting formatted time
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

import calendar

cal = calendar.month(2015, 1)
print "Here is the calendar:"
print cal
print ("------------------------------------------------------\n")


# ---------------------------------------------------
                #10th PROGRAM
                #WORKING WITH def(FUNCTION);

print ("------------------------------------------------------\n")
print("\t\t#10th PROGRAM \n")
print("\t\t#WORKING WITH def\n")
print ("------------------------------------------------------\n")

#----------------------------------------------------





def printme( string='null',*vararray):
   return {"key":string,"p2":vararray};


print printme("HI",15,155,"adfasdf");



# ---------------------------------------------------
                #11th PROGRAM
                ## Import built-in module math;

print ("------------------------------------------------------\n")
print("\t\t#11th PROGRAM \n")
print("\t\t## Import built-in module math\n")
print ("------------------------------------------------------\n")

#----------------------------------------------------



import math

content = dir(math)

print content




# ---------------------------------------------------
                #12th PROGRAM
                ## Opening and Closing Files;

print ("------------------------------------------------------\n")
print("\t\t#12th PROGRAM \n")
print("\t\t## Opening and Closing Files\n")
print ("------------------------------------------------------\n")

#----------------------------------------------------

#  CREATE FILE DETAILS AND READING  # 
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");
print "Name of the file: ", fo.name ,"\n"
print "File No : ", fo.fileno(),"\n"
fo.close()
print "Closed or not : ", fo.closed,"\n"
print "Opening mode : ", fo.mode,"\n"
print "Softspace flag : ", fo.softspace,"\n"



try:
  # open file stream
  file_name = "r.txt"
  file = open(file_name, "w")
  file.write("HI")	
except IOError:
  print "There was an error writing to", file_name



# ---------------------------------------------------
                #13th PROGRAM
                ## CLASSES;

print ("------------------------------------------------------\n")
print("\t\t#13th PROGRAM \n")
print("\t\t## CLASSES\n")
print ("------------------------------------------------------\n")

#----------------------------------------------------
  
class Networkerror(RuntimeError):
  def __init__(self, arg):
    self.args = arg
	  
try:
   print "HI ";	
   print Networkerror("Bad hostname")
except NameError,e:
   print e.args 



class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
#delattr(empl, 'age')    # Delete attribute 'age'
del emp1.age  # Delete 'age' attribute.


"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount	  

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

	
	  
   
   

