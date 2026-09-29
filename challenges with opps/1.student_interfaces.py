import statistics
class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark


    def student_average_mark(self):
        average = statistics.mean(self.mark)
        print(f"Average mark: {average}")



student1 = Student("Mirtik joy Molsom",[23,45,67,89])
print(student1.name)
student1.student_average_mark()