"""Tests for pwgen.py"""

import string
from unittest.mock import patch

import pytest

from pwgen import pwgen


class TestPwgen:
    """Tests for the pwgen function."""

    @pytest.mark.parametrize("length", [12, 15, 20, 25, 30, 45, 52])
    def test_password_length_is_exact(self, length):
        """Password length should match the requested length exactly."""
        with patch("builtins.input", return_value=str(length)):
            password = pwgen()
        assert len(password) == length

    @pytest.mark.parametrize("length", [12, 20, 35, 52])
    def test_first_character_is_digit(self, length):
        """First character should always be a digit."""
        with patch("builtins.input", return_value=str(length)):
            password = pwgen()
        assert password[0] in string.digits

    @pytest.mark.parametrize("length", [12, 20, 35, 52])
    def test_second_character_is_symbol(self, length):
        """Second character should always be a punctuation symbol."""
        with patch("builtins.input", return_value=str(length)):
            password = pwgen()
        assert password[1] in string.punctuation

    @pytest.mark.parametrize("length", [12, 20, 35, 52])
    def test_third_character_is_letter(self, length):
        """Third character should always be a letter."""
        with patch("builtins.input", return_value=str(length)):
            password = pwgen()
        assert password[2] in string.ascii_letters

    def test_password_contains_all_character_types(self):
        """Password should contain lowercase, uppercase, digits, and symbols."""
        with patch("builtins.input", return_value="20"):
            password = pwgen()

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
        with patch("builtins.input", return_value="20"):
            passwords = [pwgen() for _ in range(5)]

        # All passwords should be unique
        assert len(set(passwords)) == 5

    def test_minimum_length_boundary(self):
        """Minimum length of 12 should work correctly."""
        with patch("builtins.input", return_value="12"):
            password = pwgen()
        assert len(password) == 12

    def test_maximum_length_boundary(self):
        """Maximum length of 52 should work correctly."""
        with patch("builtins.input", return_value="52"):
            password = pwgen()
        assert len(password) == 52
