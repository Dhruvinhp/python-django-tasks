def logical_negation(num):
    return (num ^ 1) & 1


num = int(input("Enter a number: "))

result = logical_negation(num)
print("Logical negation of", num, "is", result)
