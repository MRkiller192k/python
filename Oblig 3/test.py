def  greet(name, year, rating):
    print("hey there")
    print("welcome, " + name + " year, " + year + rating)

greet("mikkel", "100", "10")
greet("iskrem", "120", "12")
greet("hei", "100", "14")


def my_function(value1, value2):
    result = value2 + value2
    return result

try:
    value1 = float(input("enter float value 1: "))
    value2 = float(input("enter float value 2: "))
    result = my_function(value1, value2)
    #do something with the result
except ValueError:
    print("not a float value")