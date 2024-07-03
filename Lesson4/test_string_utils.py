import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('input, result', [
    ("katya","Katya"),
    ("светлана", "Светлана"),
    ("", ""),
    ("%&%^&", "%&%^&"),
    ("строка с пробелом", "Строка с пробелом")
    ])
def test_capitilize_positive(input, result):
    string_utils = StringUtils ()
    res = string_utils.capitilize(input)
    assert res == result

def test_capitilize_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

@pytest.mark.parametrize( 'input, result', [
    ("  word", "word"),
    ("  слово","слово"),
    ("", ""),
    ("  111", "111"),
    ("  #$%^", "#$%^"),
    ("   Beautiful Lie", "Beautiful Lie")
])
def test_trim(input, result):
    string_utils = StringUtils()
    res = string_utils.trim(input)
    assert res == result

def test_trim_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

@pytest.mark.parametrize( 'input, result', [
    ("q,w,e,r,t,y", ["q", "w", "e", "r", "t", "y"]),
    ("1,2,3,4,5,6", ["1", "2", "3", "4", "5", "6"]),
    ("#,&,#", ["#", "&", "#"])
])
def test_to_list(input, result):
    string_utils = StringUtils()
    res = string_utils.to_list(input)
    assert res == result

def test_to_list_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

@pytest.mark.parametrize( 'input, input2, result', [
    ("flowers", "w", "floers"),
    ("Цветы", "ы", "Цвет"),
    ("#$%^", '#', "$%^"),
    ("From yesterday", "m", "Fro yesterday"),
    ("Строка с пробелом", " ", "Строкаспробелом")
])
def test_delete_symbol(input, input2, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input, input2)
    assert res == result

def test_delete_symbol_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

@pytest.mark.parametrize( 'input, input2, result', [
    ("Cat", "C", True),
    ("Cat", "t", False),
    ("123456", "1", True),
    ("123456", "4", False),
    ("$$%^&", "$", True),
    ("Paramore Decode", "e", False)
])
def test_starts_with(input, input2, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input, input2)
    assert res == result

def test_starts_with_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

@pytest.mark.parametrize( 'input, input2, result', [
    ("book", "b", False),
    ("cake", "e", True),
    ("123456", "1", False),
    ("%^&%", "%", True),
    ("Война и мир", "р", True)
])
def test_end_with(input, input2, result):
    string_utils = StringUtils()
    res = string_utils.end_with(input, input2)
    assert res == result

def test_end_with_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

@pytest.mark.parametrize( 'input, result', [
    (" ", True),
    ("Mua", False),
    ("12567", False),
    ("$%^&", False),
    ("", True )
])
def test_is_empty(input, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(input)
    assert res == result

def test_is_empty_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)

@pytest.mark.parametrize( 'input, input2, result', [
    ((["Pika", "Pika"]), "-", "Pika-Pika"),
    ((["Пика", "Пика"]), "-", "Пика-Пика"),
    ((["20", "30"]), "/", "20/30"),
    ((["С", " запятой"]), ",", "С, запятой")
])
def test_list_to_string(input, input2, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input, input2)
    assert res == result

def test_list_to_string_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitilize(None)