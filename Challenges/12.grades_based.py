numb = int(input("please enter your marks: "))

def grades_Base(nmb):
    if numb >= 90 and numb <= 100:
        return "Grade A"
    elif numb >= 75:
        return "Grade B"
    elif numb >= 65:
        return "Grade C"
    elif numb >= 30:
        return "Grade D"
    else:
        return "Grade F"

grades = grades_Base(numb)
print(grades)
        
