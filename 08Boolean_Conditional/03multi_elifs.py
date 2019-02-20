print("Give a rating on my work(out of 5)!")
rate = int(input())

if rate is 5:
    print("Excellent")
elif rate is 4:
    print("Very Good")
elif rate is 3:
    print("Good")
elif rate is 2:
    print("Not Good")
elif rate is 1:
    print("Bad")
else:
    print("Rating should be in 1 to 5")