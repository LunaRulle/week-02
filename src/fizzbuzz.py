import sys
try:
    input = int(sys.argv[1])
except ValueError:
    print("Please provide a valid number as argument!")
    exit()
if input < 0:
    print("Plase provide a positive intager")
    exit()
else:
    pass
word1 = "Fizz"
word2 = "Buzz"

def mod_of_3(number):
    if number % 3 == 0:
        return True
    else: 
        return False

def mod_of_5(number):
    if number % 5 == 0:
        return True
    else: 
        return False


for x in range(input):
    x += 1
    if mod_of_3(x) and mod_of_5(x) == True:
        print(word1 + word2)
    elif mod_of_5(x) == True:
        print(word2)
    elif mod_of_3(x) == True:
        print(word1)
    else:
        print(x)
