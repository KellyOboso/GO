

number = 67 #integer
second = 45.98 #float
greeting = "hello there" #string
ispythoninteresting = True #boolean
ispythonnotinteresting = False #boolean

#Data Structures - Multiple values stored in a single variable
cars = ["Toyota","Nissan", "vw"]#List - Ordered and changeable
fruits = ("banana", "apple", "mangle")#Tuple- ordered and unchangeable
countries = {"Kenya", "Tunisia", "Algeria"}#Set-Unordered and unchangeable
student = {
    "firstname" : "Jane",
    "age" : "25",
    "course" : "Web Development",
    "gender" : "female",
}#dictionary- key-value pair


print(cars)
print(fruits)
print(countries)
print(student)
print(student["gender"])



print(number)
print(second)
print(ispythoninteresting)

#Determining datatype - Converting from one datatype to another
print(type(countries))
print(type(student))

#Typecasting
print(float(number))
print(int(second))
