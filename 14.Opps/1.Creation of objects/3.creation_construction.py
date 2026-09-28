# class Student:

#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(self.name)


# s1 = Student("Mirtik")
# s2 = Student("Achyut")

# s1.display()
# s2.display()

class Student:
    def __init__(self,name,age):
        print("adding new student to database")
        self.name = name
        self.age = age
        

    def display(self):
        print(self.name,self.age)
        # print(self.age)

s1 = Student("Mirtik joy MOlsom", 25)
s1.display()
s2 = Student("Achyut Heqgrive",24)
s2.display()