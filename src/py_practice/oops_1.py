class Dog:
	species = "Canis familiaris"
	def __init__(self, name, age):
   		self.name = name
   		self.age = age

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)

print("Miles age is %d" % miles.age)

class Car:
	def __init__(self, name, make):
		self.name = name
		self.make = make


fortuner = Car("Fortuner", "Toyota")
alto = Car("Alto", "Maruti Suzuki")

p = alto.name
q = alto.make

print("I own a {} and it's built by {} ".format(p,q))
