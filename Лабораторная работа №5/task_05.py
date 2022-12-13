def get_random_password() -> str:
    import random
    import string
    p = 8
    password_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(random.sample(password_sym, p))
    return password

print(get_random_password())
