age = 30 #Integers
weight = 70.87 #Float
greeting = "Hola" #String
isMammal = True #Boolean

#Data Structures - Multiple elements in one variable

fruits = ["Banana", "Mango", "Orange"]#List - a list is ordered and changeable - different datatypes
courses = ["MIT", "DataScience", "Cybersecurity"] #Array -Similar datatypes
cars = ("Ford", "BMW", "G-Wagon") #Tuple - elements ordered and unchangeable
countries = {"China", "Italy", "India"} #set - unordered unchangeable
student ={
    "Firstname" : "John",
    "Course" : "MIT",
    "age" : 20,
    "Nationality" : "Kenyan"
} #Dictioanary - Key value pair

print("student is", age, "years old")
print(weight)
print("is animal a mammal? :", isMammal)
print(fruits)
print(countries)

#Typecasting changing one datatype to another
print(float(age))
print(int(weight))