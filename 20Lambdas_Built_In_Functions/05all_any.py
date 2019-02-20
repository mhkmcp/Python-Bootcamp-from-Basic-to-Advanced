names = ["Charlie", "Casey", "Codie", "Cristina"]
is_all_C = all([name[0] == 'C' for name in names])

names_ = names
names_.append("Draike")
is_any_not_C = any([name[0] != 'C' for name in names_])

print(is_all_C)
print(is_any_not_C)