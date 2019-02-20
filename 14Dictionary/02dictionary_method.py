
person = {
    'first_name': "Humayun",
    'last_name': "Kabir",
    'age': 25,
    'sex': "Male",
    'married': False
}

# copy: copy a dictionary
individual = person.copy()
print(individual)

print(person is individual)
print(person == individual)

# clear: delete everything
individual.clear()
print(individual)

# fromkeys
new_user = {}.fromkeys(['name', 'score', 'email'], 'unknown')
print(new_user)

# get
name = person.get('first_name') # returns value of the key
email = person.get('email')     # doesn't exist: None
print(email)

# pop
person.pop('married')   # pop out the k-v pair of the given key
print(person)

# popitem
print(person.popitem())  # pop randomly one item
print(person)

# update
individual.update(person)
print(individual)