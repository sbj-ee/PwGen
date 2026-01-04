# PwGen

A simple password generator that creates strong passwords with guaranteed character type placement.

## Features

- Generates passwords between 12 and 52 characters
- First 3 characters are always: digit, symbol, letter (ensures compatibility with password policies)
- Mix of lowercase, uppercase, digits, and symbols (~60% letters, ~40% digits/symbols)
- Exact length matching (no off-by-one errors)

## Usage

```bash
python pwgen.py
```

You'll be prompted to enter the desired password length (12-52 characters).

## Example

```
$ python pwgen.py
How many characters do you want in your password (max 52)? 20
Strong Password:  7#kB9xM!pL2@nQwE4$jR
len is 20
```

## Running Tests

```bash
pytest test_pwgen.py -v
```

## Requirements

- Python 3.6+
- pytest (for running tests)
