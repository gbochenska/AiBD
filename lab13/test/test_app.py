#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from app import hello, extract_sentiment, text_contain_word, bubblesort


testdata = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output



def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want



testdata = [[1,2,6,7,3,10], [4,7,2,3,11,8,99,4], [2,4,3,54,6,57,34,3,231,1,332454,32,2,22,21,32,4,5,5]]

@pytest.mark.parametrize('sample', testdata)
def test_bubblesort(sample):
    I_sort = bubblesort(sample)
    assert I_sort == sorted(sample)

