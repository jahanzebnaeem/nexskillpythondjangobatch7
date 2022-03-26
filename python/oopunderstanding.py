# SCOPE
# x = 25
#
# def my_func():
#     x = 50
#     return x
#
# # print(x)
# # a = my_func()
# # print(a)
# a = my_func()
# print(a)

# Enclosing function locals
# name = 'This is a global name!'
#
# def greet():
#     name = "Jahanzeb"
#
#     def hello():
#         print("hello " + name)
#
#     hello()
#
# greet()
# print(name)

# x = 50
#
# def func(x):
#     print('x is : ', x)
#     x = 10000
#     print('local x changed to : ', x)
#
# func(x)
# print(x)

# x = 50
#
# def func():
#     # x = 1000
#     global x
#     x = 10000
#
# print('before function call, x is : ', x)
# func()
# print('after function call, x is : ', x)

# OOP
# Class, Object & Instance (Done)

# Enumirations

# OOP Pillars
# Inheritance (Done)
    # Parent-Child
# Polymorphism (Done)
    # Same method but different implementation
# Encapsolation (Done)
    # Ease of use
# Abstraction (Done)
    # Ease out

# Constructor & Destroctor (Done)
# Overloading & Overriding
# Generaization & Specialization
# Methods & Functions (Done)
# Attributes (Done)
# Getter Setter
# Abstract class
# Instance Variable

# Relationships
# Association
# Composition
# Aggrigation


# mylist = [1,2,3]
# mylist.append(4)
# print(mylist)

# class Sample():
#     pass
#
# x = Sample()
# print(type(x))

# class Dog():
#
    # def __init__(self):
    #     pass

#
# mydog = Dog()
# print(type(mydog))

# class Dog():
#
#     def __init__(self, breed):
#         self.breed = breed
#
# mydog = Dog(breed = "Lab")
# otherdog = Dog(breed="Huskie")
# print(mydog.breed)
# print(otherdog.breed)

# class Dog():
#
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
# # mydog = Dog(breed = "Lab", name = "Bunny")
# mydog = Dog("Lab", "Bunny")
# print(mydog.breed)
# print(mydog.name)

# class Dog():
#
#     # CLASS OBHECT ATTRIBUTE
#     species = "mammal"
#
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
# mydog = Dog("Lab", "Bunny")
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)

# class Circle():
#
#     pi = 3.140
#
#     def __init__(self,radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius*self.radius*Circle.pi
#
#     def set_radius(self,new_radius):
#         self.radius = new_radius
#
# myc = Circle(3)
# # # # print(myc.radius)
# # # print(myc.area)
# # myc.radius = 100
# myc.set_radius(999)
# print(myc.area())

# INHERITANCE
# class Animal():
#
#     def __init__(self):
#         print("ANIMAL CREATED")
#
#     def whoAmI(self):
#         print("ANIMAL")
#
#     def eat(self):
#         print('EATING')
#
# class Dog(Animal):
#
#     def __init__(self):
#         # Animal.__init__(self)
#         print("DOG CREATED")
#
#     def bark(self):
#         print("WOOF")
#
#     def eat(self):
#         print("DOG EATING")
#
#
# # mya = Anima()
# # mya.whoAmI()
# # mya.eat()
# mydog = Dog()
# mydog.whoAmI()
# mydog.eat()
# mydog.bark()

# SPECIAL METHODS
# mylist = [1,2,3]
# print(mylist)

# len([1,2,3])

# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return "Title : {}, Author: {}, Page: {}".format(self.title, self.author, self.pages)
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print("a book is destroyed")
#
#
# b = Book("Python", "Jahanzeb", 200)
# # print(b)
# # print(len(b))
# del b
