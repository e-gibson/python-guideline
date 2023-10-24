# datatype that stores multiple values

courses = ["MIT", "Cybersecurity", "Data Science"]

print(courses)
# accessing elements in an array
print(courses[1])

# looping an array
for course in courses:
    print(course)

# add new element in arrays
courses.append("Android Development")
print(courses)

# removing an element from an array
courses.remove("MIT")
print(courses)

