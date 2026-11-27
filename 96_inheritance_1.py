#single level inheritance 
#parent/super/base class 
class Person:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")

# derived class 
class Student(Person):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDo(self):
        #calling parent class function
        super().walk()
        super().talk()
        self.read()
        self.write()

#object-name = ClassName()

p1 = Person()
p1.talk()
p1.walk()

s1 = Student()
s1.whatICanDo()
s1.walk()
s1.talk()
s1.read()
