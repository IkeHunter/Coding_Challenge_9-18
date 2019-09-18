"""
Create a program that finds the sum of all the numbers
between 1 and 1000 that are divisible by 3 or 5.

OUTPUT: 233168
"""

multiples = []
multiples_sum = 0

for i in range(3, 1000, 3):
    multiples.append(i)

for j in range(5, 1000, 5):
    if j not in multiples:
        multiples.append(j)

for num in multiples:
    multiples_sum += num

print(multiples_sum)

