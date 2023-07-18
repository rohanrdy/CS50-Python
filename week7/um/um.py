import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\bum\b", s, re.IGNORECASE)) # \b can be learnt at "https://docs.python.org/3/library/re.html#regular-expression-syntax:~:text=of%20the%20string.-,%5Cb,-Matches%20the%20empty"


if __name__ == "__main__":
    main()