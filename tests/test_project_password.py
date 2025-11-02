import pytest
import string
import sys
import os

# добавляем родительскую папку проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project_password import(
    make_charset,
    generate_password,
)

def test_make_charset_defaults():
    s = make_charset()
    assert any(c.isalpha() for c in s)
    assert any(c.isdigit() for c in s)




def test_make_charset_specials_only():
    s = make_charset(use_letters=False, use_digits=False, use_specials=True)
    assert s == string.punctuation




def test_generate_password_length_and_chars():
    charset = 'ab12'
    pw = generate_password(6, charset)
    assert len(pw) == 6
    assert all(ch in charset for ch in pw)




def test_generate_password_invalid_length():
    with pytest.raises(ValueError):
        generate_password(0, 'abc')




def test_generate_password_empty_charset():
    with pytest.raises(ValueError):
        generate_password(4, '')