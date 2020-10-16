import random
import string

from fastapi import Header


def generate_random_guid():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=8))


async def valid_content_length(content_length: int = Header(..., lt=65000)):
    return content_length
