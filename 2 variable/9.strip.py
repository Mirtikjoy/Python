course = "   Data engineering  "
course_Org_length = len(course)
print(course_Org_length)

required_Length = course.strip()
required_Course_length = len(required_Length)
print(required_Course_length)
print(course)

number_Of_Spaces = course_Org_length - required_Course_length
is_Clean = course_Org_length == required_Course_length

print(f"Number of spaces: {number_Of_Spaces}")
print(f"Is my Data clean: {is_Clean}")