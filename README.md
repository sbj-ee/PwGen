# PwGen

A simple password generator that creates strong passwords with guaranteed character type placement.

## Features

- Generates passwords between 12 and 52 characters
- First 3 characters are always: digit, symbol, letter (ensures compatibility with password policies)
- Mix of lowercase, uppercase, digits, and symbols (~60% letters, ~40% digits/symbols)
- Exact length matching (no off-by-one errors)
- Quiet mode for scripting

## Installation

```bash
git clone https://github.com/sbj-ee/PwGen.git
cd PwGen
pip install -r requirements.txt  # Only needed for running tests
```

## Usage

```bash
# Specify length via command line
python pwgen.py -l 20
python pwgen.py --length 20

# Quiet mode - output password only (useful for scripting)
python pwgen.py -l 20 -q
python pwgen.py -l 20 --quiet

# Interactive mode (prompts for length)
python pwgen.py
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-l`, `--length` | Password length (12-52). Prompts interactively if not specified. |
| `-q`, `--quiet` | Output password only, no extra text. |
| `-h`, `--help` | Show help message. |

## Examples

```
$ python pwgen.py -l 20
Strong Password:  7#kB9xM!pL2@nQwE4$jR
len is 20

$ python pwgen.py -l 20 -q
7#kB9xM!pL2@nQwE4$jR

$ python pwgen.py
How many characters do you want in your password (12-52)? 25
Strong Password:  3@Yp8mK!xL2#nQwE4$jRtB5&v
len is 25
```

## Running Tests

```bash
pytest test_pwgen.py -v
```

## Requirements

- Python 3.10+
- pytest (for running tests)
