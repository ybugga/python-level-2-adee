"""
Given a user's input of n, return a list of factorials from 0! to n!

Test cases:
0! = 1
1! = 1
2! = 1 x 2 = 2
4! = 1 x 2 x 3 x 4 = 24
"""


# Helper method to test equality
def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


# Todo: Create a function that produces the factorial of a number
def factorial(number):
    if number >= 0:
        result = 1
        for i in range(number,1,-1):
            result *= i
        return result
    else:
        raise ValueError("Factorial can be done for inputs >= 0")

# Todo: Test factorial function
assert_equals(factorial(0),1)
assert_equals(factorial(1),1)
assert_equals(factorial(2),2)
assert_equals(factorial(4),24)

# Todo: Request a number from the user
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid number")

# Todo: Print a list of factorials from 0 to the given number
for i in range(0,int(number)+1):
    print(f"Factorial of {i} is {factorial(i)}")
