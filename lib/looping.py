#!/usr/bin/env python3

def happy_new_year():
    k = 10
    while k>0:
        print(k)
        k -=1
    print("Happy New Year!")

def square_integers(int_list):
     list_obj = [num*num for num in int_list]
     return list_obj


def fizzbuzz():
    k = 1
    while(k<=100):
        if k % 3 == 0 and k % 5 == 0:
            print("FizzBuzz")
            k +=1
        elif k % 3 == 0:
            print("Fizz")
            k +=1
        elif k % 5 == 0:
            print("Buzz")
            k +=1
        else:
            print(k)
            k +=1
            