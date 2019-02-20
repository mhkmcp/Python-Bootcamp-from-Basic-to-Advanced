def exponent(num, power=2):     # default parameter
    return num ** power


print(exponent(3, 2))
print(exponent(4))
print(exponent(5))
# keyword arguements
print(exponent(power=3, num=4))


def add(a, b):
    return a + b


def subtract(a, b):
    return abs(a-b)


def math(a, b, fn = add):
    return fn(a, b)


print(math(3, 4))
func = add
print(math(3, 4, func))
func = subtract
print(math(3, 4, func))