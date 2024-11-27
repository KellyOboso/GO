#Built-in Functions

y=max(34, 56, 78, 18)
print(y)

x=min(34, 56, 78, 18)
print(x)

z=pow(2,3)
print("The result is",z)

#User-defined functions
def greeting():
    print("Hello there!")

greeting() #Calling Function

def multiply():
    a=12
    b=10
    print(a*b)
multiply() #Calling the Function


#Parameters and Arguments
def add(x , y):
    print(x+y)

add(4, 5) #Calling the function
add(68, 70)

def employee(fullname,age,position,status):
    print(fullname,age,position,status)

employee("Mark Joe",28,"IT","single")
employee("Jane Anne",36,"HR","single")
employee("Job Harry",25,"Clerk","Married")
employee("Mary Mbotela",29,"receptionist","married")



