# foobar
# x, y = 3, 0
# try:
#     x = x / y
#     print(x)
# except:
#     print("Divided By Zero")
# print("After Try")

d = {'mhkm': "Sylhet"}


def get(d, key):
    try:
        return d[key]
    except KeyError:
        print("Key Didn't Match")


print(get(d, "zibakapa"))
print(get(d, "mhkm"))

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number")
else:
    print("ELSE/this is a number")
finally:
    print("this is Finally")


def divide(a, b):
    try:
        return a / b
    # except ZeroDivisionError:
    #     print("Can't divide by Zero!")
    # except TypeError as err:
    #     print("a & b must be int or float")
    #     print(err)
    except (ZeroDivisionError, ValueError) as err:
        print("Something Went Wrong!")
        print(err)


print(divide(4, 2))
print(divide(3, "0"))
print(divide(3, 0))