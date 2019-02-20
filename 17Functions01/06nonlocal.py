def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

print(outer())