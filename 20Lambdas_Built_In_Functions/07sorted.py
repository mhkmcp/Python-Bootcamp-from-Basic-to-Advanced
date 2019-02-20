nums = [16, 12, 3, 54, 5]

print(sorted(nums))
print(nums)
nums.sort()
print(nums)
print(sorted(nums, reverse=True))

users =[
    {'username': "samuel", 'tweets': ["I love cake", "i love pie"]},
    {'username': "katie", 'tweets': ["I love cat"]},
    {'username': "jeff", 'tweets': []},
    {'username': "bob123", 'tweets': []},
    {'username': "dogg_luvre", 'tweets': ["Dogs are best"]},
    {'username': "guiter_gal", 'tweets': []}
]


print(sorted(users, key=lambda user: user['username']))
print(sorted(users, key=lambda user: len(user['tweets'])))
