# Tests for Q09 — Functions with Default Parameters

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from Q09 import greet, power


# --- greet tests ---

def test_greet_default():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_custom():
    assert greet("Bob", "Hi") == "Hi, Bob!"


def test_greet_another():
    assert greet("Charlie", "Hey") == "Hey, Charlie!"


# --- power tests ---

def test_power_default_exp():
    assert power(5) == 25


def test_power_custom_exp():
    assert power(2, 10) == 1024


def test_power_base_1():
    assert power(1, 100) == 1


def test_power_exp_0():
    assert power(7, 0) == 1


def test_power_exp_1():
    assert power(3, 1) == 3
