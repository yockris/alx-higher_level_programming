#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if s == "":
            s = i
        print(s, end=" ")
