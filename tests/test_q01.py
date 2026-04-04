# Tests for Q01 — Grade Calculator


def test_grade_a(run):
    output = run("Q01.py", "95\n")
    assert "A" in output


def test_grade_a_boundary(run):
    output = run("Q01.py", "90\n")
    assert "A" in output


def test_grade_b(run):
    output = run("Q01.py", "85\n")
    assert "B" in output


def test_grade_c(run):
    output = run("Q01.py", "75\n")
    assert "C" in output


def test_grade_d(run):
    output = run("Q01.py", "65\n")
    assert "D" in output


def test_grade_f(run):
    output = run("Q01.py", "40\n")
    assert "F" in output


def test_grade_f_zero(run):
    output = run("Q01.py", "0\n")
    assert "F" in output


def test_invalid_above_100(run):
    output = run("Q01.py", "105\n")
    assert "invalid" in output.lower()


def test_invalid_negative(run):
    output = run("Q01.py", "-5\n")
    assert "invalid" in output.lower()
