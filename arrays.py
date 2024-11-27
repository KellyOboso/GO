courses = ["MIT","Data Science","Cybersecurity"]
print(courses)

#Accessing an element in array
print(courses[1])

#Looping through an array
for y in courses:
    print("Course is",y)

#Adding a new element
courses.append("Android Development")
print(courses)
for y in courses:
    print("Course is",y)

#Deleting an element
courses.remove("MIT")
for x in courses: print(x)





