import pytest
from .check_text import check_text


@pytest.mark.soap
def test_step(set_words, set_urlsoap):
    good_word, wrong_word = set_words
    assert good_word in check_text(wrong_word, wsdl=set_urlsoap)