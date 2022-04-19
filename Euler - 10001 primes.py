# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


i = 2
j = 2
PrimeCheck = 1
PrimeCount = 0

while PrimeCount < 10001:
    j = 2
    PrimeCheck = 1
    while j < i:
        if i % j == 0:
            PrimeCheck = 0
            break
        j = j + 1 
    if PrimeCheck == 1:
        PrimeCount = PrimeCount + 1
        print (i, "is prime. It's the", PrimeCount , "th prime number.") 
    i = i + 1

    
 

    