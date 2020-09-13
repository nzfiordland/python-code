# Program name: CalcPi
# Author: DJO
# Date created: 2019-11-18
# Python version: 3.8

from decimal import Decimal, getcontext
import math

numberofdigits = int(input("Please enter the number of decimal place to calculate Pi to: "))
getcontext().prec = numberofdigits

def calc(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(math.factorial(6*k))*(13591409+545140134*k)
        deno = math.factorial(3*k)*(math.factorial(k)**Decimal(3))*(640320**(3*k)) 
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return str(pi)
    
print(calc(1))