# Тестовый проект для понимания GitHub

def add(x, y):
    return x + y


def do_twice(add, x, y):
    return add(add(x, y), add(x, y))


a = 5
b = 6

r = do_twice(add, a, b)

print(r)
