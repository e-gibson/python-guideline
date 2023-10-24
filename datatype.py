# Data type

number = 25  # int
second = 56.78  # float
text = "hello there"  # str
ispythoninteresting = True  # bool

# store multiple values in a single variable
cars = ["toyota", "nissan", "vw"]  # List - ordered and changeable
fruits = ("banana", "orange", "apple")  # tuple - ordered and unchangeable
countries = {"Kenya", "Tunisia", "Algeria"}  # Set - unordered and unchangeable
details = {
    "firstname": "Eva",
    "age": 20,
    "course": "Web Development",
    "nationality": "Kenyan"
}  # Dictionary - key-value pair

print(details["course"])
print(details["age"])
print(second)
print(text)
print(ispythoninteresting)
print(cars)
print(countries)
print(details)

# determine a datatype
print(type(number))
print(type(details))
print(type(countries))

# Typecasting - converting one datatype to another
print(float(number))
print(int(second))