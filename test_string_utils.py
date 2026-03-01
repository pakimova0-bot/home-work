from typing import Literal

import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize('input_text, input_symbol, expected_output',
                         [
                             ('Test', 'T', 'st'),
                             ('Test', 't', 'est'),
                             ('123456', '4', '123'),
                             ('123456', '56', '123'),
                                                      ])
def test_delete_symbol_positive(input_text, input_symbol, expected_output) :
    my_test = StringUtils()
    assert my_test.delete_symbol(input_text, input_symbol) == expected_output

@pytest.mark.parametrize('input_text, input_symbol, expected_output',
                         [
                             ('Test', 'W', 'Test'),
                             ('Test', 'H', 'Test'),
                             ('123456', '0', '123'),
                             ('123456', '90', '123'),
                             ('test string', 'c', 'test string'),
                             ('', 'a', ''),
                             (' ', 'a', ' '),
                             ('', '', ''),
                             ('   ', '   ', '   ')
                                                      ])
def test_delete_symbol_negative(input_text, input_symbol, expected_output) :
    my_test = StringUtils()
    assert my_test.delete_symbol(input_text, input_symbol) == expected_output




