# Fibonacci Sequence:
# Write a program that generates and prints the Fibonacci sequence up to a given number of terms. 
# Prompt the user for the number of terms and then calculate and display the sequence.

# Prompt for the number of terms 
terms = int(input("Enter the number of terms to display in the Fibonacci sequence: "))

"""
In the Fibonacci sequence, each number is the sum of the two preceding ones, starting from 0 and 1. 
The code below initializes two variables, a and b, with the values 0 and 1, respectively.

The line a, b = 0, 1 is a multiple assignment statement in Python.
It assigns the value 0 to the variable a and the value 1 to the variable b. 
This is a convenient way to initialize multiple variables with specific values in a single line.

Next, the line fib_sequence = [a, b] creates a list called fib_sequence and assigns it the initial values of a and b.
The list is initialized with the values 0 and 1, representing the first two terms of the Fibonacci sequence.

By starting with [0, 1], the code sets up a base or starting point for generating the Fibonacci sequence. 
This allows the subsequent terms of the sequence to be calculated and appended to the list fib_sequence 
using a loop or other iterative approach.
"""

# create a sequence
a, b = 0, 1
fib_sequence = [a, b]

# create the loop and iterate 
for _ in range(terms - 2):
    a, b = b, a + b
    fib_sequence.append(b)

# print the sequence
print(f"Fibonacci sequence: {fib_sequence}")
