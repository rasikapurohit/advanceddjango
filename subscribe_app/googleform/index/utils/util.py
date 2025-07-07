# function to generate a token
import random
import string

def generate_token(length=10)->str:
    """Generate a random token of specified length."""
    characters = string.ascii_letters + string.digits
    token = ''.join(random.choice(characters) for _ in range(length))
    return token