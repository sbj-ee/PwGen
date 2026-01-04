"""
A password generator
The passwords will be between 12 and 52 characters.
First 3 characters are always: digit, symbol, letter.
"""

import argparse
import random
import string


def generate_password(length: int) -> str:
    """Generate a password of the specified length.

    Args:
        length: Password length (must be between 12 and 52)

    Returns:
        Generated password string
    """
    if length < 12 or length > 52:
        raise ValueError("Password length must be between 12 and 52")

    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    # Reserve first 3 characters: digit, symbol, letter
    first_digit = random.choice(s3)
    first_symbol = random.choice(s4)
    first_letter = random.choice(s1 + s2)

    # Calculate remaining length to fill
    remaining_length = length - 3

    # Build pool from remaining characters (60% letters, 40% digits/symbols)
    letters_count = round(remaining_length * 0.6)
    digits_symbols_count = remaining_length - letters_count

    # Split evenly between lower/upper and digits/symbols
    lower_count = letters_count // 2
    upper_count = letters_count - lower_count
    digits_count = digits_symbols_count // 2
    symbols_count = digits_symbols_count - digits_count

    # Build the remaining characters (with replacement to handle any length)
    remaining = []
    remaining.extend(random.choices(s1, k=lower_count))
    remaining.extend(random.choices(s2, k=upper_count))
    remaining.extend(random.choices(s3, k=digits_count))
    remaining.extend(random.choices(s4, k=symbols_count))

    # Shuffle remaining characters
    random.shuffle(remaining)

    # Build final password: digit + symbol + letter + shuffled remainder
    return first_digit + first_symbol + first_letter + "".join(remaining)


def get_length_interactive() -> int:
    """Prompt user for password length interactively."""
    while True:
        user_input = input(
            "How many characters do you want in your password (12-52)? "
        )
        try:
            length = int(user_input)
            if 12 <= length <= 52:
                return length
            print("Your number should be at least 12 and no more than 52.")
        except ValueError:
            print("Please enter a valid number.")


def pwgen(length: int | None = None) -> str:
    """Generate and display a password.

    Args:
        length: Password length. If None, prompts interactively.

    Returns:
        Generated password string
    """
    if length is None:
        length = get_length_interactive()

    password = generate_password(length)
    print("Strong Password: ", password)
    print(f"len is {len(password)}")
    return password


def main():
    parser = argparse.ArgumentParser(description="Generate a strong password")
    parser.add_argument(
        "-l", "--length",
        type=int,
        choices=range(12, 53),
        metavar="12-52",
        help="Password length (12-52). If not specified, prompts interactively.",
    )
    args = parser.parse_args()
    pwgen(args.length)


if __name__ == "__main__":
    main()
