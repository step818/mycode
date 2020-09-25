#!/usr/bin/env python3

"""
Author: Stephen Trewick

This is an RPG addition to my instructors RPG for learning purposes
"""

# THINGS I'VE ADDED
# More Rooms, items lists, noticeables lists, and secrets list to each room
# The player can 'inspect noticeable' as a command. e.g. 'inspect bookcase'
# secrets lists are like items that can only be shown after inspection.
# e.g. 'inspect fireplace' might return a print--> "You see an oil canister"
# Since the items are lists, a for loop checks inside each list

def showIntro():
    # print out the opening scene to the player
    print('''You were finishing up some python practice one evening\n when ''')
    

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  inspect[noticeable]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "items" in rooms[currentRoom]:
      for item in rooms[currentRoom]['items']:
          print('You see a ' + item + '\n')
  if "noticeables" in rooms[currentRoom]:
      for thing in rooms[currentRoom]['noticeables']:
          print('You notice a ' + thing + '\n')
  print("---------------------------")

def describeNoticeable():
    print('You see a \n')
    for item in rooms[currentRoom]['secrets']:
        print(f' {item} \n')

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Foyer' : { 
                  'south' : 'Field',
                  'east' : 'Living Room',
                  'north' : 'Dining Room',
                  'west' : 'Hall',
                  'noticeables': ['Knight Armor'],
                },
            'Hall' : {
                  'north' : 'Kitchen',
                  'west' : 'Staircase (floor 1)'
                },
            'Staircase (floor 1)' : {
                'up' : 'Under Construction',
                'down' : 'Dungeon'
                },
            'Dungeon' : {
                'west': 'Staircase (floor 0)'
                },
            'Staircase (floor 0)' : {
                'up' : 'Hall'
                },
            'Kitchen' : {
                'south' : 'Hall',
                'east' : 'Dining Room'
                },
            'Dining Room' : {
                'east' : 'Living Room',
                'south' : 'Foyer',
                'west' : 'Kitchen',
                'noticeables' : ['Fireplace'],
                'secrets' : ['Oil Canister']
                },
            'Living Room' : {
                'south' : 'Gallery',
                'west' : ['Dining Room', 'Foyer']
                },
            'Gallery' : {
                'north' : 'Living Room',
                'south' : 'Library',
                'items' : ['Sword']
                },
            'Library' : {
                'north' : 'Gallery',
                'noticeables' : ['Bookcase']
                }
         }

#start the player in the Hall
currentRoom = 'Foyer'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
  # if they type 'inspect' first
  if move[0] == 'inspect' :
    if 'noticeables' in rooms[currentRoom] and move[1] in rooms[currentRoom]['noticeables']:
      #Describe what is seen with closer inspection
      describeNoticeable()
    else:
        print("That is not in this room")
  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "items" in rooms[currentRoom] and move[1] in rooms[currentRoom]['items']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
    
