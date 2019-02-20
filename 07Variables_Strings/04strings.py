single_qoute = 'hello'
double_qoute = "hello"
print(single_qoute)
print(double_qoute)

qoute = 'he said, "hello there!"'
print(qoute)
qoute = "he said, 'hello there'"
print(qoute)

qoute = "he said, \"hello there!\""
print(qoute)

#string concatenation
username = "mhkm"
msg = "Hello " + username
print(msg)

#Formatting String
name = "Humayun"
msg = f"Hello Mr. {name} Welcome!"
msg2 = "Hello Mr. {} Welcome!".format(name)
print(msg)
print(msg2)
