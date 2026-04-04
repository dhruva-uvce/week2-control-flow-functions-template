# Tests for Q02 — Leap Year Checker


def test_leap_2024(run):
    output = run("Q02.py", "2024\n")
    assert "leap year" in output.lower()
    assert "not" not in output.lower()


def test_not_leap_1900(run):
    output = run("Q02.py", "1900\n")
    assert "not" in output.lower()


def test_leap_2000(run):
    output = run("Q02.py", "2000\n")
    assert "leap year" in output.lower()
    assert "not" not in output.lower()


def test_not_leap_2023(run):
    output = run("Q02.py", "2023\n")
    assert "not" in output.lower()


def test_leap_400(run):
    output = run("Q02.py", "400\n")
    assert "leap year" in output.lower()
    assert "not" not in output.lower()


def test_not_leap_100(run):
    output = run("Q02.py", "100\n")
    assert "not" in output.lower()
