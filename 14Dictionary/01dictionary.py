person = {
    'first_name': "Humayun",
    'last_name': "Kabir",
    'age': 25,
    'sex': "Male",
    'married': False
}

print(person['first_name'])
print(person['sex'])

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key} : {value}")

if 'sex' in person.values():
    print("Yes, it have!")