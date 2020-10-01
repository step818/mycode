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
import os
import threading
import neows02

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

  show - to show current status
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
                  'south' : 'Gatehouse',
                  'north' : 'Dining Room',
                  'west' : 'Hall',
                  'noticeables': ['knight armor'],
                  'secrets': ['key']
                },
            'Hall' : {
                  'north' : 'Kitchen',
                  'west' : 'Staircase (floor 1)'
                },
            'Staircase (floor 1)' : {
                'up' : 'Bottlery',
                'down' : 'Dungeon'
                },
            'Bottlery' : {
                'down' : 'Hall',
                'north': 'Buttery',
                'south': 'Solar'
                },
            'Buttery' : {
                'south': 'Bottlery',
                'east': 'Bed Chambers'
                },
            'Solar' : {
                'north': 'Bottlery',
                'west': 'Wardrobe',
                'noticeables' : ['crystal ball']
                },
            'Wardrobe' : {
                'east' : 'Solar'
                },
            'Dungeon' : {
                'west': 'Staircase (floor 0)',
                'south' : 'Oubliette',
                'noticeables' : ['lock']
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
                'noticeables' : ['fireplace'],
                'secrets' : ['match'],
                'items': ['letter']
                },
            'Living Room' : {
                'south' : 'Gallery',
                'west' : 'Dining Room'
                },
            'Gallery' : {
                'north' : 'Living Room',
                'south' : 'Library',
                'items' : ['sword']
                },
            'Library' : {
                'north' : 'Gallery',
                'noticeables' : ['bookcase'],
                'secrets' : ['candle', 'silver key']
                },
            'Gatehouse' : {
                'north' : 'Foyer'
                }
         }

# declare all the locked doors
lockedRooms = ['Gallery', 'Solar', 'Oubliette']

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
        repeat = False
      else:  
        #set the current room to the new room
        currentRoom = nextRoom
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')
      repeat = False
  
  def t1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))

  def t2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))

  # if they type 'inspect' first
  if move[0] == 'inspect' :
    if "noticeables" in rooms[currentRoom] and move[1] in rooms[currentRoom]['noticeables']:
      # Check if the Lock is being inspected
      if (move[1] == 'lock'):
        password = input(f"Passcode: \n")
        if (password == '2009KK8'):
          # unlock the Oubliette to the monster
          print("You unlocked a secret door!")
          repeat = False
          continue
        else:
          print("That did\'nt seem to unlock anything.")
          continue
      if (move[1] == 'crystal ball'):
        # Get the message from Nasa
        print("The ball starts glowing, some misty-looking characters start forming in to familiar letters, lets look closer...")
        # Sleep timer
        neows02.main()
        continue
      # Dont loop back to showStatus()
      repeat = False
      #Describe what is seen with closer inspection
      describeNoticeable()
    elif (move[1] in rooms[currentRoom]['items']):
        print(f"I might be able to use this {move[1]} later, but there\'s nothing to inspect")
        repeat = False
    else:
        print("That\'s not in here")
        repeat = False

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "items" in rooms[currentRoom] and move[1] in rooms[currentRoom]['items']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      repeat = False
      #delete the item from the listm
      rooms[currentRoom]['items'].pop(rooms[currentRoom]['items'].index(move[1]))
    # also, if the player gets a secret item
    elif "secrets" in rooms[currentRoom] and move[1] in rooms[currentRoom]['secrets']:
      inventory += [move[1]]
      print(move[1] + ' got!')
      rooms[currentRoom]['secrets'].pop(rooms[currentRoom]['secrets'].index(move[1]))
      repeat = False
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      repeat = False
    
  if move[0] == 'use':
    use()
    repeat = False

  if move[0] == 'show':
    repeat = True

  def removeInv(item):
    inventory.pop(inventory.index(item))
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))

  def removeLRoom(room):
    lockedRooms.pop(lockedRooms.index(room))
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))

  def use():
    if move[1].lower() in inventory:
    # check if door can be unlocked with move[1]
    # if move[1] == 'key' and locked == True\
      if move[1] == 'key':
        try:
          if (rooms[currentRoom]['south']):
            nextRoomSouth = rooms[currentRoom]['south']
            if (move[1] =='key' and nextRoomSouth in lockedRooms):
              removeLRoom(nextRoomSouth)
              removeInv(move[1])
              print(f"A {move[1]} unlocked a door to the {nextRoomSouth}")
            else:
              print(f"{move[1]} doesn\'t seem to be useful here")
        except:
          print("There aren\'t any locked doors in here")
      elif move[1] == 'silver key':
        try:
          if (rooms[currentRoom]['south']):
            nextRoomSouth = rooms[currentRoom]['south']
            if (move[1] == 'silver key' and nextRoomSouth in lockedRooms):
              t1 = threading.Thread(target=removeLRoom, args=(nextRoomSouth, ), name='t1')
              t2 = threading.Thread(target=removeInv, args=(move[1], ), name='t2')
              t1.start()
              t2.start()
              t1.join()
              t2.join()
              print(f"A {move[1]} unlocked a door to the {nextRoomSouth}")
            else:
              print(f"{move[1]} doesn\'t seem to be useful here")
        except:
            print("There aren\'t any locked doors in here")
      elif move[1].lower() == 'letter':
        print(" To whom it may concern, \n the password to the safe is the name of \n the hazardous object potentially about \n  to destoy the world.")
        removeInv(move[1])
      elif (move[1] in inventory):
        print(f"I don\'t see how this {move[1]} would be useful now")
    else:
      print(f"You don\'t have a {move[1]}")


