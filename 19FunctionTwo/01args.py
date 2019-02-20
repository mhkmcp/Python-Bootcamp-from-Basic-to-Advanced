def sum_all(num1, num2, num3):
    return num1+num2+num3


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all(4, 6, 7))
print(sum_all(4, 6, 7, 2, 7, 12, 15, 32))