import subprocess
import sys
import os
import pytest


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "..")


@pytest.fixture
def run():
    """Fixture that returns a helper to run a student script with given stdin."""

    def _run(script_name, input_text=""):
        script_path = os.path.join(TEMPLATE_DIR, script_name)
        result = subprocess.run(
            [sys.executable, script_path],
            input=input_text,
            capture_output=True,
            text=True,
            timeout=10,
        )
        assert result.returncode == 0, (
            f"{script_name} crashed:\n{result.stderr}"
        )
        return result.stdout

    return _run
