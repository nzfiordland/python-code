import random

# generate random numbers 1 - 6
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1
randomNumber = random.randrange(1000) + 1

total = die1 + die2

print (sorted([4,2,7,4,2,8,6,9,8,3,4,7]))

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print (a),
        a, b = b, a+b

# Now call the function we just defined:
fib(2000)

print(3*6)
print(range(10))

print(range(5, 10))

print(range(0, 10, 3))

a = ['Mary', 'had', 'a', 'little', 'lamb', 'it''s', 'fleece', 'was', 'white', 'as', 'snow' ]
for i in range(len(a)):
    print (i, a[i])

print (3+3*4)

print ("You rolled a", die1, "and a", die2, "for a total of", total)
print (randomNumber)

input("Press the enter key to exit.")
