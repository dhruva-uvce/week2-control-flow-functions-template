# Tests for Q04 — Star Pattern


def _extract_star_lines(output):
    """Extract the star pattern lines, stripping any input() prompt text."""
    lines = []
    for raw in output.splitlines():
        # Keep only the portion from the first '*' onward
        idx = raw.find("*")
        if idx != -1:
            lines.append(raw[idx:].strip())
    return lines


def test_pattern_5_rows(run):
    output = run("Q04.py", "5\n")
    lines = _extract_star_lines(output)
    assert len(lines) == 5
    for i, line in enumerate(lines, start=1):
        assert line == "*" * i


def test_pattern_3_rows(run):
    output = run("Q04.py", "3\n")
    lines = _extract_star_lines(output)
    assert len(lines) == 3
    for i, line in enumerate(lines, start=1):
        assert line == "*" * i


def test_pattern_1_row(run):
    output = run("Q04.py", "1\n")
    lines = _extract_star_lines(output)
    assert len(lines) == 1
    assert lines[0] == "*"
