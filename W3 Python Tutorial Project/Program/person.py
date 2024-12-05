class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return (f'{p1.name} is {p1.age}') 
  
  def greeting(self):
    print("Hello my name is " + self.name)


p1 = Person("John", 36)

print()
print(p1)
print()
p1.greeting()
print()

class Student(Person):
  def __init__(self, fname, age, year):
    super().__init__(fname, age)
    self.graduationyear = year
  
  def welcome(self):
    print("Welcome", self.name, self.age, "to the class of", self.graduationyear) 

x = Student("Mike", 27, 2019)
print(f'{x.name} is {x.age} with a graduation year of {x.graduationyear}\n ')
x.welcome()
print()
x = Student("Olsen", 23, 2019)
print(f'{x.name} is {x.age} with a graduation year of {x.graduationyear} \n ')
x.welcome()
print()