# Write a program to print "Hello world!"
from math import sqrt


print('Hello world!')


# Write a program to accept input from user and print it
userInput = input('Message: ')
print(userInput)

# Write a program to add two numbers
x = 10
y = 20
print(x + y)

# Write a program to input two numbers from user and add them
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print(x + y)

# Write a program to input a number from user and change it's symbol
x = int(input('Enter a number: '))
x = -x
print(x)

# Write a program to check if a number is positive or negative

# Solution 1:
x = int(input('Enter a number: '))
if x == 0:
    print("It's Zero!")
elif abs(x) != x:
    print("It's negative!")
else:
    print("It's positive!")

# Solution 2:
x = int(input('Enter a number: '))
if x == 0:
    print("It's Zero!")
elif x > 0:
    print("It's positive!")
else:
    print("It's negative!")

# Write a program to check if a person is eligible to vote

# Solution 1: Basic
age = int(input('Enter your age: '))
if age >= 18:
    print("You're eligible")
else:
    print("You're not eligible")

# Solution 2: Advanced
age = int(input('Enter your age: '))
if abs(age) != age:
    print("You aren't born yet...")
elif age < 18:
    print("You're not eligible")
elif age >= 18 and age < 110:
    print("You're eligible to vote")
else:
    print("You're too old to live on Earth...")

# Write a program to find area of square
s = int(input('Enter side: '))
if abs(s) != s:
    print('Side cannot be negative!')
else:
    print(f'Area: {s**2} sq units')

# Write a program to find area of rectangle
l = int(input('Enter length: '))
b = int(input('Enter breadth: '))
if l>0 and b>0:
    print(f'Area: {l*b} sq units')
else:
    print('You cannot have negative sides!')


# Write a program to check if the given three sides can form a traingle or not
x = int(input('Enter first side: '))
y = int(input('Enter second side: '))
z = int(input('Enter third side: '))

if x>0 and y>0 and z>0:
    if x+y>z and y+z>x and x+z>y:
        print('It can form a triangle')
    else:
        print('It cannot form a traiangle')
else:
    print('It cannot form a triangle')


# Write a program to find area of triangle
import math
x = int(input('Enter first side: '))
y = int(input('Enter second side: '))
z = int(input('Enter third side: '))

if x>0 and y>0 and z>0:
    if x+y>z and y+z>x and z+x>y:
        if x == y == z:
            print(f'Area: {(math.sqrt(3)/4)*x**2} sq units')
        else:
            s = (x+y+z)/2
            print(f'Area: {math.sqrt(s*(s-x)*(s-y)*(s-z))} sq units')
    else:
        print('Given dimensions cannot form a triangle!')
else:
    print('You cannot have negative sides!')


# Write a program to calculate simple interest
p = int(input('Enter principal amount: '))
r = int(input('Enter rate (%) : '))
t = int(input('Enter time (pa) : '))

print(f'Simple interest: {(p*r*t)/100} rupees')


# Write a program about rolling a dice
import random
print(f'You got : {random.randint(1, 6)}')


# Write a program to check if a number is prime or not
num = int(input('Enter number: '))
checkList = []
for x in range(2, num):
    if num % x == 0:
        checkList.append(x)
if len(checkList) >= 1:
    print(f"It's not prime and is divisible by {len(checkList) + 2} numbers")
else:
    print("It's prime")


# Write a program to find the HCF of two numbers
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
xPrime = x
yPrime = y
check = True

if x > y:
    while check == True:
        if x%y == 0:
            print(f'HCF({xPrime}, {yPrime}) = {y}')
            check = False
        else:
            oldx = x
            oldy = y
            x, y = oldy, oldx%oldy
else:
    print('x should be greater than y')


# Write a program to find area and circumference of circle
import math

r = int(input('Enter radius: '))
print(f'Area: {math.pi*r**2} sq units')
print(f'Circumference: {2*math.pi*r} sq units')


# Write a program to print the sum of first n natural numbers
n = int(input('Enter n: '))
result = 0

for x in range(1, n+1):
    result += x

print(f'Sum: {result}')

# Write a program to swap two elements in a list
mainList = ['tony', 'mony', 'sony']
oldElement = input('Enter old element: ')
newElement = input('Enter new element: ')

if oldElement.lower() in mainList:
    i = mainList.index(oldElement)
    mainList[i] = newElement
    print(mainList)
else:
    print("Item does not exist in the list!")


# Write a program to reverse a list
mainList = ['1', '2', '3', '4', '5']
mainList.reverse()
print(mainList)


# Write a program to print all positive numbers in a list
mainList = [1, 2, 3, 4, -5, -6, 7, -8, 9, 10]
newList = []
for item in mainList:
    if abs(item) == item:
        newList.append(item)

for newItem in newList:
    print(newItem)


# Make a game: Rock, Paper, Scissors
import random

botScore = 0
userScore = 0
chance = 1
chances = 3
choiceList = ['r', 'p', 's']

while chance <= chances:
    botChoice = random.choice(choiceList)
    userChoice = input('Choose (R) (P) (S)? : ')

    if userChoice.lower() in choiceList:


        if userChoice.lower() == botChoice:
            print(f"""
It's a tie!
User score: {userScore}
Bot score: {botScore}
===============================

""")

        elif userChoice.lower() == 'r' and botChoice == 'p':
            botScore += 1
            chance += 1
            print(f"""
Bot won!
User score: {userScore}
Bot score: {botScore}
Chances remaining: {chances-(chance-1)}
===============================

""")

        elif userChoice.lower() == 'p' and botChoice == 'r':
            userScore += 1
            chance += 1
            print(f"""
User won!
User score: {userScore}
Bot score: {botScore}
Chances remaining: {chances-(chance-1)}
===============================

""")
        elif userChoice.lower() == 's' and botChoice == 'r':
            botScore += 1
            chance += 1
            print(f"""
Bot won!
User score: {userScore}
Bot score: {botScore}
Chances remaining: {chances-(chance-1)}
===============================

""")
        elif userChoice.lower() == 'r' and botChoice == 's':
            userScore += 1
            chance += 1
            print(f"""
User won!
User score: {userScore}
Bot score: {botScore}
Chances remaining: {chances-(chance-1)}
===============================

""")
        elif userChoice.lower() == 'p' and botChoice == 's':
            botScore += 1
            chance += 1
            print(f"""
Bot won!
User score: {userScore}
Bot score: {botScore}
Chances remaining: {chances-(chance-1)}
===============================

""")
        elif userChoice.lower() == 's' and botChoice == 'p':
            botScore += 1
            chance += 1
            print(f"""
Bot won!
User score: {userScore}
Bot score: {botScore}
Chances remaining: {chances-(chance-1)}
===============================

""")

    else:
        print('Invalid input!')

if userScore == botScore:
    print(f"""
--------------------------
Result!                  |
--------------------------
It's a tie!              |
User score: {userScore}  
Bot score: {botScore}    
--------------------------
""")

elif userScore > botScore:
    print(f"""
--------------------------
Result!                  |
--------------------------
User won!                |
User score: {userScore}  
Bot score: {botScore}    
--------------------------
""")
else:
    print(f"""
--------------------------
Result!                  |
--------------------------
Bot won!                 |
User score: {userScore}  
Bot score: {botScore}    
--------------------------
    """)
