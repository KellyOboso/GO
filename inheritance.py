#Parent Class
class Animal:
    def speak(self):
        print("Animal is speaking")

#Child Class
class Dog(Animal): #inheritance
    def bark(self):
        print("Dog is barking")

a = Animal()


d=Dog()
d.speak()





