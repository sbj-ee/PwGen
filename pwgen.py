"""
A password generator
The passwords will be between 12 and 52 characters.
First 3 characters are always: digit, symbol, letter.
"""

import string
import random


def pwgen() -> str:
    class InvalidNumber(Exception):
        """Exception raised for invalid number entered"""

        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    # store all characters in lists
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    # Ask user about the number of characters
    user_input = input("How many characters do you want in your password (max 52)? ")

    # check this input is it number? is it more than 8?
    while True:
        try:
            characters_number = int(user_input)
            if characters_number < 12 or characters_number > 52:
                raise InvalidNumber(
                    "Your number should be at least 12 and no more than 52."
                )
            else:
                break
        except InvalidNumber:
            print("Please, Enter numbers only.")
            print("Your number should be at least 12 and no more than 52.")
            user_input = input(
                "How many characters do you want in your password (max 52)? "
            )

    # Reserve first 3 characters: digit, symbol, letter
    first_digit = random.choice(s3)
    first_symbol = random.choice(s4)
    first_letter = random.choice(s1 + s2)

    # Calculate remaining length to fill
    remaining_length = characters_number - 3

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
    password = first_digit + first_symbol + first_letter + "".join(remaining)
    print("Strong Password: ", password)
    print(f"len is {len(password)}")
    return password


if __name__ == "__main__":
    pwgen()
