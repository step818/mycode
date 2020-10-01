#!/usr/bin/env python3 
from castle import rooms

# go
def  go(direction, currentRoom):
  if (direction in rooms[currentRoom]): 
    nextRoom = rooms[currentRoom][direction]
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

# get

# inspect

# use

