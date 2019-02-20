nums = [1, 2, 3, 4, 5]
double = map(lambda x: x * 2, nums)
print(nums)
print(double)
for num in double:
    print(num, end=' ')
print()
_double = list(map(lambda x: x * 2, nums))
print(_double)

people = ["Darcy", "Christina", "Diana"]
peeps = list(map(lambda name: name.upper(), people))
print(peeps)

names = [
    {'first': "Rusty", 'last': "Steele"},
    {'first': "Colt", 'last': "Steele"},
    {'first': "Blue", 'last': "Steele"}
]

first_names = list(map(lambda name : name['first'], names))

print(names)
print(first_names)