nums = {
    'a': 1,
    'b': 2,
    'c': 3
}
sq_nums = {key: value **2 for key, value in nums.items()}
print(sq_nums)

sq_numbers = {num: num**2 for num in [1, 2, 3, 4, 5]}
print(sq_numbers)

str1 = 'ABC'
str2 = '123'
combo = {str1[i]:str2[i] for i in range(0, len(str1))}
print(combo)

num_list = [1, 2, 3, 4, 5, 6]
parity = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(parity)