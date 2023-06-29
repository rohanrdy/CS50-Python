import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        sys.exit("Too many command-line arguments")

    if file_path[-3:] == ".py":
        try:
            file = open(file_path).read().splitlines()
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            print(get_lines(file))
    else:
        sys.exit("Not a Python file")


def get_lines(file):
    count = 0
    for i in file:
        if i.strip() != "" and i.strip()[0] != "#": # strip used to account for "Assume that any line that starts with #, optionally preceded by whitespace, is a comment" and if a line has more than one whitespace
            count += 1
    return count


if __name__ == "__main__":
    main()