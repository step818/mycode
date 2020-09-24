#!/usr/bin/env python3

import requests
import random

def main():
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    
    chad_fact_list = []
    
    

    substr = "A cat"
    for cat in r.json()["all"]:
        old_fact = cat.get("text")
        if old_fact.find(substr) != -1:
            # replace the string "A cat" with a new substring
            new_fact = old_fact.replace(substr, "Chad")
            chad_fact_list.append(new_fact)

    for fact in chad_fact_list:
        print(fact)

    

main()

