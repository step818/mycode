#!/usr/bin/env python3

print("What age are you really???")
print("Choose the letter the corresponds to the best answer to the question?")

answer1 = ""
while (answer1 == ""):
    answer1 = float(input("How many alcoholic beverages do you drink  per week on average?\n"))

answer2 = ""

while (answer2 != "A" and answer2 != "B" and answer2 != "C" and answer2 != "D"):
    answer2 = input("You've been invited to a friend\'s party, and it starts at 9:30.\n Do you...\n A. Have no problem declining the invite.\n B. Show up on time, but leave at 10:30.\n C. Show up l  ate.\n D. Show up on time, and leave at 4am.\n").upper()

answer3 = ""
while (answer3 != "A" and answer3 != "B" and answer3 != "C" and answer3 != "D"):
    answer3 = input(f"You have an extra $1000, what do you do with it?\n A. Put it toward paying off credit card debt.\n B. You take a trip with friends.\n C. Spend it on {answer1} more drinks at the bar. \n D. Spend it frivolously on random things and wonder where the money went.\n").upper()

answer4 = ""
while (answer4 != "A" and answer4 != "B" and answer4 != "C" and answer4 != "D"):
    answer4 = input("Doing absolutely nothing is... \n A. A dream come true.\n B. Boring.\n C. Seemingly lazy. \n D. Not possible, I need to do something. \n").upper()

age = 0
# Check results for the first question
if answer1 >= 30:
    age += 18
elif answer1 >= 15:
    age += 25
elif answer1 >= 6:
    age += 30
elif answer1 >=0:
    age += 40
else:
    age -= 4
    print("You didn\'t provide a valid answer, seem more like a kindergartner to me.\n")

#Check the results for the second question
if (answer2 == "A"):
    age += 10
elif (answer2 == "B"):
    age += 6
elif (answer2 == "C"):
    age += 4
elif (answer2 == "D"):
    age += 0
else:
    age -= 4
    print("You did not follow directions, you really are younger than I thought.\n")

# Check the results for the third question
if (answer3 == "A"):
    age += 5
elif (answer3 == "B"):
    age += 3
elif (answer3 == "C"):
    age += 2
elif (answer3 == "D"):
    age += 0
else:
    age -= 4
    print("How did you get that wrong?\n")

# Check the results for the fourth answer
if (answer4 == "A"):
    age += 5
elif (answer4 == "B"):
    age += 3
elif (answer4 == "C"):
    age += 3
elif (answer4 == "D"):
    age += 1
else:
    age -= 4
    print("You did not follow directions, you really are younger than I thought.\n")    


print(f"Your actual age is {age}. YEEESHH! ")
