#!/usr/bin/env python3

import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json").json()

    # get the value of number of people
    numPpl = r.get("number")

    print(f"People in space: {numPpl}")
    # loop through the list of people
    for x in r.get("people"):
        print(f"{x.get('name')} on the {x.get('craft')}")
   
                
main()
