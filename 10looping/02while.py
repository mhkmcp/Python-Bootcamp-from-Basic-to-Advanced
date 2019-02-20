val = 1

while val < 20:
    print(val)
    val += 4

print("what's the password?")
msg = input()
while msg != "lana":
    print("WRONG!")
    print("what's the password?")
    msg = input()
print("CORRECT!")