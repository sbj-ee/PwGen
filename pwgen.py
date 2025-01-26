"""
A password generator
The passwords will be between 12 and 52 characters.
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

    # shuffle all lists
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    # calculate 30% & 20% of number of characters
    part1 = round(characters_number * (30 / 100))
    part2 = round(characters_number * (20 / 100))

    # generation of the password (60% letters and 40% digits & punctuations)
    result = list()
    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])

    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])

    # shuffle result
    random.shuffle(result)

    # join result
    password = "".join(result)
    print("Strong Password: ", password)
    print(f"len is {len(password)}")
    return password


if __name__ == "__main__":
    pwgen()
