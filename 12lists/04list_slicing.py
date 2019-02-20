first_list = [1, 2, 3, 4, 5, 6]
# exclusing counting
print(first_list[3:])       # [4 5 6]
print(first_list[:3])       # [1 2 3]
print(first_list[2:5])      # [3 4 5]

# [start:end:step]
print(first_list[20:])      # []
print(first_list[1::2])     # [2 4 6]
print(first_list[1:6:2])    # [2 4 6]
print(first_list[::2])      # [1 3 5]

print(first_list[1::-1])    # [2 1]
print(first_list[:1:-1])    # [6 5 4 3]
print(first_list[2::-1])    # [3 2 1]
