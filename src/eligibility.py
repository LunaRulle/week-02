can_vote = bool
can_rent = bool
senior_discount = bool
student_discount = bool
def yes_or_no(answer):
    if answer == "y":
        return True
    else:
        return False

try:
    age = int(input("what is your age? "))
except ValueError:
    print("invalid age")
    exit()
if 0 <= age <= 200:
    pass
else:
    print("invalid age")
    exit()

usr_license = yes_or_no(input("Do you have a drivers license? (y/n): "))
veteran = yes_or_no(input("Are you a veteran? (y/n): "))
student = yes_or_no(input("are you a student? (y/n): "))

if age >= 18:
    can_vote = True
else:
    can_vote = False

if age >= 18 and usr_license == True:
    can_rent = True
else:
    can_rent = False

if age >= 65 or veteran == True:
    senior_discount = True
else:
    senior_discount = False

if 16 <= age <= 26 and student == True:
    student_discount = True
else:
    student_discount = False

print(f"Voting: {can_vote} \nCar renting: {can_rent}\nSenior discount: {senior_discount}\nStudent discount: {student_discount}")
