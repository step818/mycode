#!/usr/bin/env python3
def counter():
    sink = ["cup", "spoon", "plate", "knife", "spatula"]
    action = "AAAAAGH!!!"
    
    for dish in sink:
         print(f"There\'s a dirty {dish} in the sink! {action}") 


def delete():
    hallway = ["action figure", "book", "dish", "pile of trash", "juice stain"]

    action = "whoop your ass!"

    for junk in hallway:
        print(f"There\'s a {junk} in the hallway! I\'m gonna {action}")

def add():
    report_card = ["A+", "A-", "B+","Terrific"]

    action = "buy you ice cream"

    for grade in report_card:
        print(f"You got a {grade} on your report card. I\'m going to {action}")


counter()
print("\n")
delete()
print("\n")
add()
