#!/usr/bin/env python3

# rooms
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
