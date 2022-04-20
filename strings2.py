#write a python program to perform operations on strings
name=input("enter your name")
print(type(name))
print(id(name))

#methods on strings
print(name.upper())
print(name.title())
print(name.lower())

#write a python program to perform strings concanation
first_name=input("enter your first name")
fathers_name=input("enter your fathers name")
last_name=input("enter your last name")
full_name=last_name+first_name+fathers_name
print(full_name)
