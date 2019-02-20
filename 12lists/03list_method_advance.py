


numbers = [5, 9, 5, 6, 7, 5, 8, 8, 9, 10, 15]
# index
print(numbers.index(5))         # first appearance of 5 #0
print(numbers.index(5, 3))      # first appearance of 5 after index 3 #5
print(numbers.index(9, 6, 9))   # first appearance of 5 in between index 6 & 9 #8
print()

# count()
print(numbers.count(5))     #3
print(numbers.count(14))    #0
print(numbers.count(8))     #2

# reverse()
numbers.reverse()
print("Reversed: ")
print(numbers)

# sort()
numbers.sort()
print("Sorted: ")
print(numbers)
