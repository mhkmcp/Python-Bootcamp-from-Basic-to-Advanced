maze = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in maze:
    for val in row:
        print(val, end=' ')
    print()
print(maze[2][2])
print()
print()
[[print(val) for val in row ] for row in maze]

