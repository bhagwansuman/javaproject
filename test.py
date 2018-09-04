#!usr/bin/python

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Suman", 26)
p1.myfunc()

s=raw_input("Enter a name:")
s=s[::-1]
print s
# If the number is positive, we print an appropriate message

num = 1 
if num > 0:
    print(num, "is a positive number.")
#print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a negative number.")
#print("This is also always printed.")
