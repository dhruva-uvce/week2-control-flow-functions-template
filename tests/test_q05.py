# Tests for Q05 — FizzBuzz


def _fizzbuzz_lines(output):
    """Extract just the fizzbuzz result lines, stripping any input() prompt."""
    lines = []
    for raw in output.strip().splitlines():
        text = raw.strip()
        if not text:
            continue
        # The input() prompt may prefix the first result line, e.g. 'Enter n: 1'
        # Strip everything up to and including ': ' if present
        if ": " in text:
            text = text.split(": ", 1)[1]
        lines.append(text)
    return lines


def test_fizzbuzz_15(run):
    output = run("Q05.py", "15\n")
    result_lines = _fizzbuzz_lines(output)
    assert len(result_lines) == 15
    assert result_lines[0] == "1"
    assert result_lines[1] == "2"
    assert result_lines[2] == "Fizz"
    assert result_lines[3] == "4"
    assert result_lines[4] == "Buzz"
    assert result_lines[5] == "Fizz"
    assert result_lines[9] == "Buzz"
    assert result_lines[14] == "FizzBuzz"


def test_fizzbuzz_5(run):
    output = run("Q05.py", "5\n")
    result_lines = _fizzbuzz_lines(output)
    assert result_lines[0] == "1"
    assert result_lines[2] == "Fizz"
    assert result_lines[4] == "Buzz"


def test_fizzbuzz_3(run):
    output = run("Q05.py", "3\n")
    result_lines = _fizzbuzz_lines(output)
    assert result_lines[0] == "1"
    assert result_lines[1] == "2"
    assert result_lines[2] == "Fizz"


def test_fizzbuzz_1(run):
    output = run("Q05.py", "1\n")
    assert "1" in output
