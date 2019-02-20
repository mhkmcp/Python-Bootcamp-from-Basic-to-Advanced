nums = [1, 2, 3, 4]

nums = [x*10 for x in nums]

print(nums)
print([x * 10 for x in nums])

name = 'humayun'

_name = [char.upper() for char in name]
print(_name)

friends = ["sriju", "tani", "puja"]

print([friend[0].upper() for friend in friends])
# print(my_friend)

numbers = range(1, 11)

evens = [x for x in numbers if x % 2 == 0]
odds  = [x for x in numbers if x % 2 == 1]
print(evens)
print(odds)

special = [x * 2 if x % 2 == 0 else x / 2 for x in numbers]
print(special)
