def fav_colors(**kwargs):
    ''' kwargs comes as a dictionary '''
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(sriju="red", faizu="yellow", kabir="black")


def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David"
    elif "David" in kwargs:
        return f"{kwargs['David']} David"
    return "Not sure who is this"

print(special_greeting(David='Hello'))
print(special_greeting(Bob='hey'))
print(special_greeting(David='special'))