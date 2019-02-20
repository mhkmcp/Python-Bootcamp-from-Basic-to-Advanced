nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda num : num % 2 == 0, nums))
print(even)

names = ['austin', 'penny', 'anthony', 'rihana', 'billy', 'angel']
a_names = list(filter(lambda name: name[0] == 'a', names))
print(a_names)