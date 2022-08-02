class Student:
    
    def _init__(self,name,age,admission,course):
        self.name=name
        self.age=age
        self.admission=admission
        self.course=course

    def myfunc(self):
        print("Hello my name " + s2.name)

s2=Student()
s2.name='Shadrack'
print(s2.name)
s2.myfunc()