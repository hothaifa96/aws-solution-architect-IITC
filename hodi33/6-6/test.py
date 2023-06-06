# py test
#
# QA - automation
#
# framework  - test

import pytest
import requests


def test1():  # testcase
    expected = 2
    actual = 20 % 20
    assert expected == actual


def test2():
    res = requests.get('https://gooooooooooooooogle.com')
    assert 200 <= res.status_code < 400


def test3():
    res = requests.get('https://google.com')
    assert 200 <= res.status_code < 400
