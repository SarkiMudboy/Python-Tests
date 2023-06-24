import random
from typing import Iterable

def get_random_num(scope: int) -> int:
    result = random.randint(0, scope)

    return result

def get_random_obj(scope: int) -> int:

    collection = [i for i in range(scope)]
    
    return random.choice(collection)