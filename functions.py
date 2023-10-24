# user-defined functions
def greeting():
    print("Hello World")


greeting()


def sum():
    print(6 + 7)


sum()


def details():
    print("Eva", "Web dev")


details()


# parameters and arguments
def student(firstname, course, age):
    print(firstname, course, age)


student("Eva", "Datascience", 20)
student("Mark", "Android Development", 24)
student("Job", "Computer Science", 24)

# built-in library functions
y = max(40, 13, 56, 79, 45)
print(y)

x = min(89, 90, 6, 67, 54)
print(x)