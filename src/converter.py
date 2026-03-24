KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
EUR_TO_USD = 0.84235020
conversions = ["km<->mi","kg<->lb","L<->gal","EUR<->USD"]
unit = ["km","mi","kg","lb","L","gal","EUR","USD"]
ratios = [KM_TO_MI,KG_TO_LB,L_TO_GAL,EUR_TO_USD]

print("What would you like to convert today?")
for index, item in enumerate(conversions):
    print(f"{index})", item)

try:
    user_index = int(input())
    conversions[user_index]
except IndexError:
    print("This was not an option")
    exit()
except ValueError:
    print("that is not a number")
    exit()

print("you have selected: ",conversions[user_index])
print("Please choose direction of convertion")
print("0)",unit[user_index + user_index],"->", unit[user_index + user_index + 1])
print("1)",unit[user_index + user_index + 1],"->", unit[user_index + user_index])

try:
    user_direction = int(input())
except ValueError:
    print("This was not an option")
    exit()

print(f"Please enter the amount of {unit[user_index + user_index + user_direction]} to convert")
try:
    user_amount = float(input())
except ValueError:
    print("That is not a number")
    exit()
converted_value = 0
if user_direction == 0:
    converted_value = user_amount * ratios[user_index]
elif user_direction == 1:
    converted_value = user_amount / ratios[user_index]
print(f"{converted_value:.2f}",unit[user_index + user_index])
