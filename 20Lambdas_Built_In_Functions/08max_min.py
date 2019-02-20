nums = [199, 34, 1, 763, 23, 1829, 29]
tup = (199, 34, 1, 763, 23, 1829, 29)

print(max(nums))
print(min(nums))

print(max(tup))
print(min(tup))

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']
print(min(names))
print(max(names))
ans = min(len(name) for name in names)
print(ans)

ans = min(names, key=lambda name: len(name))
print(ans)
ans = max(names, key=lambda name: len(name))
print(ans)

songs = [
    {'title': "Happy Birthday", 'play_count': 1},
    {'title': "Survive", 'play_count': 6},
    {'title': "YMCA", 'play_count': 99},
    {'title': "Toxic", 'play_count': 31},
]
print(min(songs, key=lambda song:song['play_count']))
print(max(songs, key=lambda song:song['play_count']))
print(min(songs, key=lambda song:song['play_count'])['title'])
print(max(songs, key=lambda song:song['play_count'])['title'])