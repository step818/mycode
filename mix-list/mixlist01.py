#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

challenge_list = ["awesome", "terrible", "superb", "Python", "banana", 1, 2]

print(f"{challenge_list[3]} is {challenge_list[0]}! For lunch I will have {challenge_list[6]} {challenge_list[4]}s.")
