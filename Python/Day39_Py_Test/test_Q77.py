# Install `pytest`. Write tests for your standalone functions from earlier days — at least: `factorial`, `binary_search`, `email_validator`, `flatten_list`. Each function should have at least 3 tests: one happy path, one edge case, one error case.

import pytest
from factorial import facto
from binary_search import recBinarySearch
from emailValidator import emailEval
from flattenList import flatten_list

# Factorial Test
def test_neg_num_fact():
    with pytest.raises(ValueError):
        facto(-3)

def test_zero_facto():
    assert facto(0) == 1

def test_less_then_three():
    assert facto(2) == 2

def test_more_then_two():
    assert facto(5) == 120
    assert facto(6) == 720
    assert facto(10) == 3628800


# Binary Search Test

@pytest.fixture
def sorted_list():
    return [2, 5, 8, 12, 15, 18, 21, 25, 29, 33, 37, 41, 45, 49, 53]

def test_isFound(sorted_list):
    assert recBinarySearch(sorted_list, 0, len(sorted_list) - 1, 33) == 9

def test_isNotFound(sorted_list):
    assert recBinarySearch(sorted_list, 0, len(sorted_list) - 1, 55) == -1

def test_isAtStart(sorted_list):
    assert recBinarySearch(sorted_list, 0 , len(sorted_list) - 1, 2) == 0

def test_isAtEnd(sorted_list):
    assert recBinarySearch(sorted_list, 0, len(sorted_list) - 1, 53) == 14


# Email Validator

def test_valid_email():
    assert emailEval("john.doe@gmail.com") == True

def test_invalid_double_at():
    assert emailEval("alice@@yahoo.com") == False

def test_valid_country_domain():
    assert emailEval("user_123@example.co.uk") == True

def test_invalid_domain():
    assert emailEval("mike.smith@.com") == False

def test_valid_plus_email():
    assert emailEval("contact-us+support@company.org") == True

def test_empty_email():
    assert emailEval("") == False

def test_email_with_minimal_domain():
    assert emailEval("a@b.co") == True


# Flatten List

def test_flatten_list():
    nested_list = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8],
        [9]
    ]

    assert flatten_list(nested_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_empty_list():
    assert flatten_list([]) == []

def test_single_nested_list():
    assert flatten_list([[1, 2, 3]]) == [1, 2, 3]