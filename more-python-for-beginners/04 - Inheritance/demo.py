class Person:
	def __init__(self, name):
		self.name = name
	def say_hello(self):
		print('Hello, ' + self.name)

class Student(Person):
	def __init__(self, name, school):
		super().__init__(name)
		self.school = school
	def sing_school_song(self):
		print('Ode to ' + self.school)

student = Student('Christopher', 'UVM')
student.say_hello()
student.sing_school_song()
# What are you?
print(isinstance(student, Student))
print(isinstance(student, Person))
print(issubclass(Student, Person))
