class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age





s1 = Student("Mirtik joy molsom", 25)
print(s1.name)
del s1.name
print(s1.name)