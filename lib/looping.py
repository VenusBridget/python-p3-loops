#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    count = 10
    while count > 0:
        print (count)
        count -=1
    print ("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    # code goes here!
    pass
    squares = [integer**2 for integer in int_list]
    print (squares)
    return squares
square_integers([1,2,3,4,5] and [-1,-2,-3,-4,-5])

def fizzbuzz():
    # code goes here!
    pass
    for num in range (1, 101):
        if not (num %15):
            print ('FizzBuzz')
        elif not num %3:
            print ('Fizz')
        elif not num %5:
            print ('Buzz')
        else:
            print (num)
fizzbuzz()
