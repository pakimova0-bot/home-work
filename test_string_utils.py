import pytest
from string_utils import StringUtils


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("skypro", "Skypro."),
        ("Skypro", "Skypro."),
        ("skypro eng", "Skypro Eng."),
    ],
)
def test_trim_positive(self, units, input_data, expected_result):
    assert utils.trim(input_data) == expected_result


@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")],
)
def test_process_negative(self, units, input_data, expected_result):
    processor = StringUtils()
    assert processor.process(input_text) == expected_output


@pytest.mark.positive
@pytest.mark.parametrize("input_data, expected_result", [
    ("     skypro", "Skypro"),
    ("Hello", "hello"),
    ("   skypro eng", "Skypro Eng."),
    ("", "")
])        
def contains ( self, string: str, symbol: str, [
    ("SkyPro", "F", "SyPro"),
    ("SkyPro", "O", "Sky")
    ])
@pytest.mark.parametrize (
"input_string, Symbol",
    [
        ("Hello!", "H"),
        ("123456", " "),
        ("Hello", "W")
],
)
def test_contains(Input_string, Symbol):
    Utils3=StringUtils()
    assert Utils3.contains(input_string, symbol) is True


@pytest.mark.positive
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
    assert string_utils.delete_symbol("skypro", "s") == "kypro"


@pytest.mark.negative
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
    assert string_utils.delete_symbol("skypro", "s") == "skypro"    


