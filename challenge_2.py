"""
Create a program that contains a function that takes at least 3 parameters:
the maximum range and at least 2 other numbers.
The function needs to find the sum of all the numbers within
the max range and that are divisible by any of numbers
(or if there is more than one argument, the number has to be
divisible by any of them).

INPUT: ‘function_name(3, 5)’
OUTPUT: 233168


INPUT: ‘function_name(2, 3, 8)’
OUTPUT: 333167
"""


def sum_of_multiples(*args):
    multiples = []
    multiples_sum = 0

    for arg in args:
        for i in range(arg, 1000, arg):
            if i not in multiples:
                multiples.append(i)

    for multiple in multiples:
        multiples_sum += multiple

    return multiples_sum


answer = sum_of_multiples(3, 5)  # INPUT 1
print("Answer 1: " + str(answer))  # OUTPUT 1: 233168

second_answer = sum_of_multiples(2, 3, 8)  # INPUT 2
print("Answer 2: " + str(second_answer))  # OUTPUT 2: 333167

