#!/usr/bin/env python3

easy = ["science", "turbo", ["goggles", "eyes"], "nothing"]


medium = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


hard = [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


easyEyes = easy[2][1]

easyGoggs = easy[2][0]

easyNoth = easy[3]

print(f"My {easy[2][1]}! The {easy[2][0]} do {easy[3]}! ")

medEyes = medium[2].get("goggles")

medGoggs = medium[2].get("eyes")

medNoth = medium[3]

print(f"My {medEyes}! The {medGoggs} do {medNoth}!")

hardEyes = hard[0].get('user').get('name').get('first')

hardGoggs = hard[0].get("kumquat")

hardNoth = hard[0].get("d")

print(f"My {hardEyes}! The {hardGoggs} do {hardNoth}!")

