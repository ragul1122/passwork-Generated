import random
import string

def generate_password(length=12):
    """Generate a secure and strong password.

    Args:
        length (int): Length of the password. Default is 12.

    Returns:
        str: Generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example
password = generate_password()
print("Generated password:", password)
