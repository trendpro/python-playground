"""Exploring python comprehensions."""

import pprint

printer = pprint.PrettyPrinter()

# check in num is even or odd
categories = ["Even" if num % 2 == 0 else "Odd" for num in range(20)]
# print(categories)

# Filtering a list
cool_factors = [num for num in range(3000) if num % 47 == 0]
# printer.pprint(cool_factors)

# 3D Matrix
lst = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)
    lst.append(l1)

# printer.pprint(lst)

# List comprehension equivalent
matrix = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
# printer.pprint(matrix)


# Square
def square(num):
    return num * num


squared_nums = [square(num) for num in range(100)]
# print(squared_nums)

# dictionary comprehension
data = [("a", 122), ("b", 203), ("c", 932), ("d", 171), ("e", 1028)]
dict = {k: v * v for k, v in data}
print(dict)

# generators
sum_of_squares = sum(num**2 for num in range(1000000))
print(sum_of_squares)
