import unittest
from random_gen import *

class TestRandomGenerator(unittest.TestCase):

    def test_random_num(self) -> None:
        
        scope = 'data'
        runs = 5
        fails = 0

        for _ in range(runs):

            random_num = get_random_num(scope)
            random_choice = get_random_obj(scope)

            if random_num == random_choice:
                fails += 1

        self.assertLess(fails, 2)


if __name__ == '__main__':
    unittest.main()