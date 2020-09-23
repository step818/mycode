#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]}, {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}, {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NEfarm = farms[0]['agriculture']
Wfarm = farms[1]['agriculture']
SEfarm = farms[2]['agriculture']

# display the animals on the NE farm
def easyish():
    for animal in NEfarm:
        print(animal)

# prompt the user for a farm and print the agricultural life on that farm
def medium():
    f = input("Choose one of our farms, and I'll list out the agriculture there. OPTIONS: (N, W, or, S)")
    if(f == "N"):
        for agri in NEfarm:
             print(agri)
    elif(f == "W"):
        for agri in Wfarm:
            print(agri)
    elif(f == "S"):
        for agri in SEfarm:
            print(agri)

# prompt the user for a farm and then display only the animals unique to that farm
def hard():
    f = input("Choose one of our farms, and I'll list out the agriculture there. OPTIONS: (N, W, or, S)")
    if(f == "N"):
        for agri in farm['agriculture']:
            if agri != "carrots" 



easyish()
medium()

