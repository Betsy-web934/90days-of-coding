#INHERITANCE
#practice creating parent and child classes using inheritance, method overriding and suoer() function

#create a parent class called person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def role(self):
        print(f"I am a person")

#create a student class that inherits from the parent class
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying Computer Science")

    def role(self):
        print(f"I am a student")

#create a new child class called Teacher
class Teacher(Person):
    #add a new attribute called subject
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    #create a method called teach
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

    def role(self):
        print(f"I am a teacher")

#create another child class called Principal 
class Principal(Person):
    #add a new attribute called school_name
    def __init__(self, name, age, school_name):
        super().__init__(name, age)
        self.school_name = school_name

    def manage_school(self):
        print(f"{self.name} is managing {self.school_name}")

    def role(self):
        print(f"I am a principal")


#objects
student = Student("Betsy Nashipai", 18, "Software Engineering")
teacher = Teacher("Mr. Job Murithi", 20, "Python")
principal = Principal("Mrs. Mary", 35, "Coding Time School") 

#call all the objects methods
student.introduce()
student.study()
student.role()

teacher.introduce()
teacher.teach()
teacher.role()

principal.introduce()
principal.manage_school()
principal.role()
