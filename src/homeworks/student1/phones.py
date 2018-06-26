import random

def create_phone():
    choices = "0123456789"
    return '9' + ''.join(random.choice(choices) for _ in range(9))


def generate_number_strings(n, name):
    with open(name, 'w') as f:
        for _ in range(n):
            f.write(create_phone() + '\n')
