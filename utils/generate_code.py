import random

def generate_code(length=8):
    date = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''.join(random.choice(date) for _ in range(length))
    return code