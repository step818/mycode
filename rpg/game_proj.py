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
  inspect [noticeable]
  use [item]
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
  # print a significant object in the room if there is one
  # in case the player wants to get closer for easter eggs
  if "noticeables" in rooms[currentRoom]:
      for thing in rooms[currentRoom]['noticeables']:
          print('You notice a ' + thing + '\n')
  print("---------------------------")

# Print out the secret items when player "inspects <noticeable>"
def describeNoticeable():
    if rooms[currentRoom]['secrets']:
      print('You see a \n')
      for item in rooms[currentRoom]['secrets']:
          print(f' {item} \n')
    else:
      print(f"There\'s nothing much to see on the {move[1]}")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Foyer' : { 
                  'locked' : False,
                  'south' : 'Field',
                  'east' : 'Living Room',
                  'north' : 'Dining Room',
                  'west' : 'Hall',
                  'noticeables': ['knight armor'],
                  'secrets': ['key']
                },
            'Hall' : {
                  'locked' : False,
                  'north' : 'Kitchen',
                  'west' : 'Staircase (floor 1)'
                },
            'Staircase (floor 1)' : {
                'locked' : False,
                'up' : 'Bottlery',
                'down' : 'Dungeon'
                },
            'Bottlery' : {
                'down' : 'Hall'
                },
            'Dungeon' : {
                'locked' : False,
                'west': 'Staircase (floor 0)'
                },
            'Staircase (floor 0)' : {
                'locked' : False,
                'up' : 'Hall'
                },
            'Kitchen' : {
                'locked' : False,
                'south' : 'Hall',
                'east' : 'Dining Room'
                },
            'Dining Room' : {
                'locked' : False,
                'east' : 'Living Room',
                'south' : 'Foyer',
                'west' : 'Kitchen',
                'noticeables' : ['fireplace'],
                'secrets' : ['match']
                },
            'Living Room' : {
                'locked' : False,
                'south' : 'Gallery',
                'west' : ['Dining Room', 'Foyer']
                },
            'Gallery' : {
                'locked' : True,
                'north' : 'Living Room',
                'south' : 'Library',
                'items' : ['sword']
                },
            'Library' : {
                'north' : 'Gallery',
                'noticeables' : ['bookcase'],
                'secrets' : ['candle']
                }
         }

# declare all the locked doors
lockedRooms = ['Gallery']

#start the player in the Hall
currentRoom = 'Foyer'

showInstructions()
# Sometimes, showStatus isn't necessary
repeat = True
#loop forever
while True:
    
  if(repeat):
    showStatus()
  else:
    repeat = True

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
    if (move[1] in rooms[currentRoom]):
      nextRoom = rooms[currentRoom][move[1]]
      # check if the door to the next room is locked
      if nextRoom in lockedRooms:
        print('The door to the room you\'re trying to open is locked')
      else:  
        #set the current room to the new room
        currentRoom = nextRoom
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')
  # if they type 'inspect' first
  if move[0] == 'inspect' :
    if "noticeables" in rooms[currentRoom] and move[1] in rooms[currentRoom]['noticeables']:
      # Dont loop back to showStatus()
      repeat = False
      #Describe what is seen with closer inspection
      describeNoticeable()
    elif ("items" in rooms[currentRoom]):
      print(f"There\'s nothing to inspect here, it just says \'Made in China\'")
    else:
        print("That\'s not in here")
  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "items" in rooms[currentRoom] and move[1] in rooms[currentRoom]['items']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the listm
      rooms[currentRoom]['items'].pop(rooms[currentRoom]['items'].index(move[1]))
    # also, if the player gets a secret item
    elif "secrets" in rooms[currentRoom] and move[1] in rooms[currentRoom]['secrets']:
      inventory += [move[1]]
      print(move[1] + ' got!')
      rooms[currentRoom]['secrets'].pop(rooms[currentRoom]['secrets'].index(move[1]))
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
    
  if move[0] == 'use':
    if move[1].lower() in inventory:
    # check if door can be unlocked with move[1]
    # if move[1] == 'key' and locked == True\
      try:
        if (rooms[currentRoom]['south']):
          nextRoomSouth = rooms[currentRoom]['south']
          if move[1] =='key' and nextRoomSouth in lockedRooms:
            lockedRooms.pop(lockedRooms.index(nextRoomSouth))
            inventory.pop(inventory.index(move[1]))
            print(f"A {move[1]} unlocked a door to the {nextRoomSouth}")
          else:
            print(f"{move[1]} doesn\'t seem to be useful here")
      except:
        print("There aren\'t any locked doors in here")
    else:
      print(f"You don\'t have a {move[1]}")




