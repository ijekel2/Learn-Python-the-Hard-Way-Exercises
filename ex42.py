## Animal is-a object
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## From self get the name attribute and set it to name
		self.name = name

## Cat is-a Animal
class Cat(Animal):
	
	def __init__(self, name):
		## Initialize name attribute
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## initialize name attribute
		self.name = name

## Employee is-a Person
class Employee(Person):

	def __init__(self, name):
		## initialize name attribute
		self.name = name

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## shaun is-a Cat
shaun = Cat("Shaun")

## Mary is a Person
mary = Person("Mary")

## Mary has a pet Cat
mary.pet = shaun

## frank is an employee
frank = Employee("Frank", 120000)

## frank has a pet
frank.pet = rover



