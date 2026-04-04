# Tests for Q10 — Call by Reference: List Mutations

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from Q10 import add_element, double_elements


# --- add_element tests ---

def test_add_element_basic():
    lst = [1, 2, 3]
    add_element(lst, 4)
    assert lst == [1, 2, 3, 4]


def test_add_element_empty():
    lst = []
    add_element(lst, 10)
    assert lst == [10]


def test_add_element_returns_none():
    lst = [1]
    result = add_element(lst, 2)
    assert result is None


# --- double_elements tests ---

def test_double_basic():
    lst = [1, 2, 3, 4]
    double_elements(lst)
    assert lst == [2, 4, 6, 8]


def test_double_empty():
    lst = []
    double_elements(lst)
    assert lst == []


def test_double_returns_none():
    lst = [5]
    result = double_elements(lst)
    assert result is None


def test_double_single():
    lst = [7]
    double_elements(lst)
    assert lst == [14]


# --- combined, as in the assignment ---

def test_combined_workflow():
    numbers = [1, 2, 3]
    add_element(numbers, 4)
    assert numbers == [1, 2, 3, 4]
    double_elements(numbers)
    assert numbers == [2, 4, 6, 8]
