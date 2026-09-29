class student:
    def __init__(self,name,age,address,University_Name,Enroolment_Nmber):
        self.name = name
        self.age = age
        self.address = address
        self.University_name = University_Name
        self.Enroolment_number = Enroolment_Nmber


    def welcome(self):
        print("Welcome", self.name,"to Rai University")

    def display(self):
        print("age:",self.age)
        print("Address details:",self.address)
        print("Stuent of:",self.University_name)
        print("Enrolment Number:",self.Enroolment_number)


student1 = student('Mirtik joy Molsom',23,'Tribhagya para','Rai University','24BTIT019')
student1.welcome()
student1.display()

