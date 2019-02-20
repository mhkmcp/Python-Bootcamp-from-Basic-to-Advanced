# raise ValueError("Hello It's Invalid Error!")

# raise NameError('Blah Blah Blah')


def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("Use only available color")
    print(f"Printed {text} in {color}")


colorize("hello", "cyan")
colorize("kabir", "red")