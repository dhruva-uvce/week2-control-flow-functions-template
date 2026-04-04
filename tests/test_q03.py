# Tests for Q03 — Multiplication Table


def test_table_of_5(run):
    output = run("Q03.py", "5\n")
    # Check first, middle, and last lines
    assert "5 x 1 = 5" in output
    assert "5 x 5 = 25" in output
    assert "5 x 10 = 50" in output


def test_table_of_3(run):
    output = run("Q03.py", "3\n")
    assert "3 x 1 = 3" in output
    assert "3 x 10 = 30" in output


def test_table_of_1(run):
    output = run("Q03.py", "1\n")
    assert "1 x 1 = 1" in output
    assert "1 x 10 = 10" in output


def test_table_has_10_lines(run):
    output = run("Q03.py", "7\n")
    # Count lines that match the pattern "7 x ? = ?"
    lines = [l for l in output.strip().splitlines() if "7 x" in l and "=" in l]
    assert len(lines) == 10
