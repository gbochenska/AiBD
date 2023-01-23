#!/usr/bin/python
# -*- coding: utf-8 -*-

from textblob import TextBlob


def hello(name):
    output = f'Hello {name}'
    return output

def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubblesort(I):
    n = len(I)
    liczba = 0
    sorted_list = I[:]
    while n > 1:
        for i in range(1, n):
            liczba += 1
            if sorted_list[i - 1] > sorted_list[i]:
                sorted_list[i - 1], sorted_list[i] = sorted_list[i], sorted_list[i - 1]
        n = n - 1
    return sorted_list