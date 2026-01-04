"""Tests for pwgen.py"""

import string
import subprocess
import sys

import pytest

from pwgen import generate_password, pwgen


class TestGeneratePassword:
    """Tests for the generate_password function."""

    @pytest.mark.parametrize("length", [12, 15, 20, 25, 30, 45, 52])
    def test_password_length_is_exact(self, length):
        """Password length should match the requested length exactly."""
        password = generate_password(length)
        assert len(password) == length

    @pytest.mark.parametrize("length", [12, 20, 35, 52])
    def test_first_character_is_digit(self, length):
        """First character should always be a digit."""
        password = generate_password(length)
        assert password[0] in string.digits

    @pytest.mark.parametrize("length", [12, 20, 35, 52])
    def test_second_character_is_symbol(self, length):
        """Second character should always be a punctuation symbol."""
        password = generate_password(length)
        assert password[1] in string.punctuation

    @pytest.mark.parametrize("length", [12, 20, 35, 52])
    def test_third_character_is_letter(self, length):
        """Third character should always be a letter."""
        password = generate_password(length)
        assert password[2] in string.ascii_letters

    def test_password_contains_all_character_types(self):
        """Password should contain lowercase, uppercase, digits, and symbols."""
        password = generate_password(20)

        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)

        assert has_lower, "Password should contain lowercase letters"
        assert has_upper, "Password should contain uppercase letters"
        assert has_digit, "Password should contain digits"
        assert has_symbol, "Password should contain symbols"

    def test_passwords_are_random(self):
        """Multiple calls should produce different passwords."""
        passwords = [generate_password(20) for _ in range(5)]
        assert len(set(passwords)) == 5

    def test_minimum_length_boundary(self):
        """Minimum length of 12 should work correctly."""
        password = generate_password(12)
        assert len(password) == 12

    def test_maximum_length_boundary(self):
        """Maximum length of 52 should work correctly."""
        password = generate_password(52)
        assert len(password) == 52

    def test_length_too_short_raises_error(self):
        """Length below 12 should raise ValueError."""
        with pytest.raises(ValueError, match="between 12 and 52"):
            generate_password(11)

    def test_length_too_long_raises_error(self):
        """Length above 52 should raise ValueError."""
        with pytest.raises(ValueError, match="between 12 and 52"):
            generate_password(53)


class TestPwgenFunction:
    """Tests for the pwgen wrapper function."""

    def test_pwgen_with_length_argument(self):
        """pwgen should accept length as argument."""
        password = pwgen(20)
        assert len(password) == 20


class TestCLI:
    """Tests for command line interface."""

    def test_cli_with_length_argument(self):
        """CLI should accept -l/--length argument."""
        result = subprocess.run(
            [sys.executable, "pwgen.py", "-l", "20"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "len is 20" in result.stdout

    def test_cli_with_long_length_argument(self):
        """CLI should accept --length argument."""
        result = subprocess.run(
            [sys.executable, "pwgen.py", "--length", "25"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "len is 25" in result.stdout

    def test_cli_invalid_length_too_short(self):
        """CLI should reject length below 12."""
        result = subprocess.run(
            [sys.executable, "pwgen.py", "-l", "5"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0

    def test_cli_invalid_length_too_long(self):
        """CLI should reject length above 52."""
        result = subprocess.run(
            [sys.executable, "pwgen.py", "-l", "100"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0

    def test_cli_help(self):
        """CLI should display help."""
        result = subprocess.run(
            [sys.executable, "pwgen.py", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Password length" in result.stdout

    def test_cli_quiet_flag(self):
        """CLI -q flag should output password only."""
        result = subprocess.run(
            [sys.executable, "pwgen.py", "-l", "20", "-q"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Should only contain the password (20 chars) and newline
        assert len(result.stdout.strip()) == 20
        assert "Strong Password" not in result.stdout
        assert "len is" not in result.stdout

    def test_cli_quiet_long_flag(self):
        """CLI --quiet flag should output password only."""
        result = subprocess.run(
            [sys.executable, "pwgen.py", "-l", "15", "--quiet"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert len(result.stdout.strip()) == 15
