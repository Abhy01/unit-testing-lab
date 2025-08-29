# test_your_module.py

import pytest
from your_module import safe_divide, string_analyzer

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5.0),
    (5, 0, float('inf')),
    (-10, -5, 2.0)
])
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected


@pytest.mark.parametrize("text,expected", [
    ("Hello 123", {'lowercase': 4, 'uppercase': 1, 'digits': 3, 'spaces': 1}),
    ("", {'lowercase': 0, 'uppercase': 0, 'digits': 0, 'spaces': 0}),
    ("AaBb123 ", {'lowercase': 2, 'uppercase': 2, 'digits': 3, 'spaces': 1}),
])
def test_string_analyzer(text, expected):
    assert string_analyzer(text) == expected
