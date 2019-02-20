def display_name(first, second):
    print(f"{first} says hello to {second}")


name = {'first': "Charlie", 'second': "Puth"}
# display_name(first="Charlie", second="Puth")
display_name(**name)