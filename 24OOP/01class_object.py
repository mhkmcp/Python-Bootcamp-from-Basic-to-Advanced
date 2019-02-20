class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        print("A New User Has Been Made")


user1 = User("Joe", "Smith", 28)
user2 = User("Blanca", "Lopez", 31)

print(type(user1))
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)

