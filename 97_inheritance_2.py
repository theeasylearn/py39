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


class Developer(Student):
    def code(self):
        print("I can write code")
    def debug(self):
        print("I can debug code")
    #Method Overidding
    def whatICanDo(self):
        super().whatICanDo()
        self.code()
        self.debug()

#object-name = ClassName()

d1 = Developer()
d1.whatICanDo()
d1.code()
d1.debug()