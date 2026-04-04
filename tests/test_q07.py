# Tests for Q07 — Reverse a Number


def test_reverse_1234(run):
    output = run("Q07.py", "1234\n")
    assert "4321" in output


def test_reverse_5000(run):
    output = run("Q07.py", "5000\n")
    lines = output.strip().splitlines()
    last_line = lines[-1]
    assert "5" in last_line


def test_reverse_100(run):
    output = run("Q07.py", "100\n")
    assert "1" in output


def test_reverse_single_digit(run):
    output = run("Q07.py", "7\n")
    assert "7" in output


def test_reverse_palindrome(run):
    output = run("Q07.py", "121\n")
    assert "121" in output
