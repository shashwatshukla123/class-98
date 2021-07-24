# function is block of code which only run when it is called.
from os import read, write


def myFunction():
    print("i am inside function")

myFunction()    

# function with arguments
def myFunction(name):
    print("hello"+name)

myFunction("shashwat")
myFunction("alham")

def myFunction(fname,lname):
    print("hello "+fname +"  "+lname)

myFunction("shukla","red")  

# arbitraey arguments(if you dont know how many that will be passed to your function *)
def myFunction(*names):
    print("the last element is"+names[2])
    print("hello")

myFunction("red","blue","green") 

#files handeling
#open()  takes two parameters (file name ,mode)
#r read (by Default) error if file not there
#a append (open for appending create the file not there)
#w write (open for writting create the file if not there)
#x create (create  the file , error if already there)

#filehandling mode
#"t"- by Default text mode
#"b"- binary (image files)

#open file
f=open("sample1.txt")
#same as below
f=open("sample1.txt","rt")
#open() returns a file object,wich has a read() method which read the content of the file
#print(f.read())

#by default read() return the whole text but we can specify how many characters we want to read
#print(f.read(6))

#you can return one line by using readline() method
print(f.readline())

#by looping throught the lines you an read whole file by line by line
f=open("sample1.txt","r")
for x in f:
    print(x)

#close files when you are done
f.close()     

# write to an extisting  file
#"a"-append will append to the end of the file
f=open("sample2.txt","a")
f.write("hello")
f.close()

#"w"-for overwritting the content 
f=open("sample2.txt","w")
f.write("opps i have dleted the content ")
f.close()

#open and read the file after overwritting 
f=open("sample2.txt","r")
print(f.read())

#create a new file
#f=open("myfile.txt","x")

# delete a file
#import os
#os.remove("myfile.txt")

txt = "welcome to the jungle"

x = txt.split()
print(x)