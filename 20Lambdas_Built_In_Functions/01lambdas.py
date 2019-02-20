def square(num): return num * num

# lambda : annonymous function
# only allow single expression, it is automatically returned
square2 = lambda num: num * num

add = lambda a, b : a + b

print(square2(5))
print(add(6, 7))
print(type(square2))

print(square.__name__)
print(square2.__name__)
print(add.__name__)