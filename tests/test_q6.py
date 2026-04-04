# Tests for Q6 — Factorial


def test_factorial_5(run):
    output = run("Q6.py", "5\n")
    assert "120" in output


def test_factorial_0(run):
    output = run("Q6.py", "0\n")
    assert "1" in output


def test_factorial_1(run):
    output = run("Q6.py", "1\n")
    assert "1" in output


def test_factorial_10(run):
    output = run("Q6.py", "10\n")
    assert "3628800" in output


def test_factorial_format(run):
    output = run("Q6.py", "5\n")
    assert "5!" in output
