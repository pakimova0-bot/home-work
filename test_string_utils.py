from typing import Literal
import pytest
from string_utils import StringUtils
string_utils = StringUtils()

@pytest.mark.parametrize("input_str, expected", [
                             ("skypro', 'Skypro"),
                             ("", ""),
                             ("Skypro", "Skypro"),
                             ("a", "A"),
                             ("123", "123"),
                             ("test string", "Test string"),
                             ])
def test_paramratrize(self, itils, input_str: Literal['skypro\', \'Skypro'] | Literal[''] | Literal['Skypro'] | Literal['a'] | Literal['123'] | Literal['test string'], expected: Literal['skypro\', \'Skypro'] | Literal[''] | Literal['Skypro'] | Literal['A'] | Literal['123'] | Literal['Test string']):
    assert itils.parametrize(input_str) == expected


@pytest.mark.parametrize('input_text, input_symbol, expected_output', [ 
                            ('Test', 'W', 'Test'),
                            ('Test', 'H', 'Test'),
                            ('123456', '0', '123'),
                            ('123456', '90', '123'),
                            ('test string', 'c', 'test string'),
                            ('', 'a', ''),
                            (' ', 'a', ' '),
                            ('', '', ''),
                            ('   ', '   ', '   ')])

def test_delete_symbol_negative(input_text, input_symbol, input_output):
    my_test = StringUtils()
    assert my_test.delete_symbol(input_text, input_symbol) ==  expected_output
