# Task: Given a number (positive, negative, or 0), return the logical negation (as a 1 or 0) of that
# number. Do so using only bitwise operators. Any of these characters/constructs are not allowed
# if, do, while, for, -, not, or, and, is, [,] and any functions.


def logical_negation(num):
    return (num ^ 1) & 1


num = int(input("Enter a number: "))

result = logical_negation(num)
print("Logical negation of", num, "is", result)
