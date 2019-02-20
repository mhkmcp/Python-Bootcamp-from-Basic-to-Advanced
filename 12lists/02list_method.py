# append: add one item to the list
# extend: add more than one item to the list
# insert: add one item at a given position
# clear: remove all items from the list
# demo: remove last element or element in the given position
# remove: remove the first appearance of a given number

list = []
list.append(70)
list.append(16)
list.append(37)
print(list)

list_one = [1, 2, 4]
list_two = [5, 6, 7, 8]
list_one.insert(2, 3)
print(list_one)

# list_one.append(list_two)
list_one.extend(list_two)
print(list_one)

demo = list_two
print(demo)
demo.clear()
print(demo)


demo = list_one
print(demo.pop())
print(demo.pop(1))

nums = [1, 3, 4, 6, 5, 4]
nums.remove(4)
print(nums)