'''
1. parameters
2. *args
3. default parameters
4. **kwargs
'''

def display_info(a, b, *args, inst="Kabir", **kwargs):
    return [a, b, args, inst, kwargs]

print(display_info(1, 2, 3, name="Humayun", job="Teacher"))
'''
a - 1
b - 2
args - (3,)
inst - "Kabir"
kwargs - {'name': "Humayun", 'job': "Teacher"
'''