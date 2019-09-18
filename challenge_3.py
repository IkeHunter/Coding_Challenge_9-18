"""
Create a program that accepts two inputs: a max range, and multiple numbers.
The program needs to have a function that finds the sum of all the numbers
within the max range that are divisible by all of the numbers from the second input.
The program must properly handle errors and not break.

INPUT:  > ‘1000’
        > ‘3, 5’
OUTPUT: 33165


INPUT:  > ‘10’
        > ‘2’
OUTPUT: 20


INPUT:  > ‘10000’
        > ‘2, 3, 4, 6’
OUTPUT: 4168332
"""


def factor_sum(max_range, args):
    numbers = []
    numbers_sum = 0

    for i in range(1, max_range):
        state = True
        if i not in numbers:
            for arg in args:
                if is_factor(i, arg) is not True:
                    state = False
                    break
            if state is True:
                numbers.append(i)

    if len(numbers) == 0:
        return 0, 0
    else:
        for number in numbers:
            numbers_sum += number

        return numbers_sum, numbers


def is_factor(number, factor):
    if number % factor == 0:
        return True
    else:
        return False


input_range = input("Enter the max range: ")  # first INPUT
max_int_range = False

while True:
    try:
        max_int_range = int(input_range)
        break
    except ValueError:
        input_range = input("Max range must be an int: ")
        continue


input_factors = input("Please enter common factors followed by ',': ")  # second INPUT
factors_string_list = input_factors.split(', ')
factors_int_list = []

while True:
    try:
        for num in factors_string_list:
            factors_int_list.append(int(num))
        break
    except ValueError:
        input_factors = input("Factors must be an int: ")
        factors_string_list = input_factors.split(', ')
        continue

if max_int_range and factors_int_list:
    answer_int, answer_list = factor_sum(max_int_range, factors_int_list)
    if not answer_int == 0 and not answer_list == 0:
        print("Answer: {}, Numbers with these common factors: {}".format(answer_int, answer_list))  # OUTPUT
    else:
        print("There were no numbers with these common factors")

else:
    print("Something strange happened")


