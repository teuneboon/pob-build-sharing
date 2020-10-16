import random
import string


def generate_random_guid():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=8))
