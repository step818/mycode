#!/usr/bin/env python3

def main():
    howBig = int(input(f"Pick a smallish number please: "))

    stri = ""
    for star in range(howBig):
        stri += "*"
        print(stri)

    for star in stri:
        howBig -= 1
        print(stri[0:howBig])

main()
