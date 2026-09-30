class parent:
    def display(self):
        print("This is parent method")


class child(parent):
    def Cjild_display(self):
        print("This is child method")


person = child()
print(person.display())
print(person.Cjild_display())
