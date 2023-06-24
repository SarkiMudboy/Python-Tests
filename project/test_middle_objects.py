from collections.abc import Iterable
from typing import Any
import unittest



class TestGetMid(unittest.TestCase):

    def test_first_case(self) -> None:

        data = [1, 2, 3, 'six', 'seven']
        result = 5
        
        self.assertEqual(mid_obj(data),  result, 'Required output: ' + str(result))

    def test_dict_case(self) -> None:

        list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        dict_data = {str(k): k for k in list_data}

        result = 4
        
        self.assertEqual(mid_obj(dict_data, True),  result, 'Required output: ' + str(result))


def mid_obj(data: Iterable, is_dict: bool=False) -> Any:

    obj_length = len(data)

    mid_pos = obj_length // 2

    if is_dict:

        index = str(mid_pos)
        result = data[index]
        
    else:
        result = data[mid_pos]

    return result

def test_mid_obj(test_data: Iterable, result: Any) -> None:

    assert mid_obj(test_data) == result, 'Required output: ' + str(result)


if __name__ == "__main__":
    
    unittest.main()