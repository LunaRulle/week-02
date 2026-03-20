print("Here are some of the data types python has")
text = "hello"
number = 4
decimal = 2.75
boolean = True
empty = None 
data_types = [text, number, decimal, boolean, empty]

for item in data_types:
    print(f"{item} is a", type(item))
print(f"{data_types} is a",type(data_types))

print("You can also convert between type but they need to make sense! \nhere are some examples:")
print("float to int",int(decimal))
print("bool to int",int(boolean))
print("int to float",float(number))
print("bool to float",float(boolean))
print("str to bool",bool(text))
print("NoneType to bool",bool(empty))

print("Some data types you can't convert between for example")
print("str to int or float, as long as the string contains letters")

for item in data_types:
    print(bool(item))
