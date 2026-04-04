# Tests for Q08 — Sum of Digits


def test_sum_9876(run):
    output = run("Q08.py", "9876\n")
    assert "30" in output


def test_sum_100(run):
    output = run("Q08.py", "100\n")
    assert "1" in output


def test_sum_5(run):
    output = run("Q08.py", "5\n")
    assert "5" in output


def test_sum_999(run):
    output = run("Q08.py", "999\n")
    assert "27" in output


def test_sum_1234(run):
    output = run("Q08.py", "1234\n")
    assert "10" in output
