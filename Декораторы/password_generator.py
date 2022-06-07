import random
import string


# написать декоратр, который будет
# принимать функцию password_generator
# и возвращать сложность пароля:
# слабый - есть только буквы или только цифры
# средний - есть и цифры и буквы
def decorator(func):
    def wrapper():
        password = func()
        print(password)
        if password.isdigit() or password.isalpha():
            return "слабый"
        else:
            return "средний"

    return wrapper


@decorator
def password_generator():
    numbers = string.ascii_letters
    digits = string.digits
    all = list(numbers + digits)
    number = random.randint(1, 10)
    random.shuffle(all)
    return ''.join(all[:number])


print(password_generator())
