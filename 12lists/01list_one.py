my_list = ["musa", 25, True, 45.678]

print(my_list)
print(len(my_list))

for item in my_list:
    print(item, end=' ')
print()

r = range(1, 10)
print(r)
print(list(r))

colors = ["purple", "teal", "magenta", "blue"]

# iterate using for-loop
for color in colors:
    print(color, end=' ')
print()

# iterate using while loop
x = 0
while x < len(colors):
    print(colors[x], end=' ')
    x += 1