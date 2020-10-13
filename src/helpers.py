import random
import string


def get_random_int(length=1):
    """
    Return random number given length
    by default len=1
    """
    return ''.join(str(random.randint(0, 9)) for i in range(length))


def get_random_str(length=1):
    let = string.ascii_lowercase
    return ''.join(random.choice(let) for _ in range(length))


def get_random_email(length=1):
    """
    """
    return '@'.join([get_random_str(length), get_random_str(length)])
