def main():
    while True:
        try:
            f = input("Fraction: ")
            x = convert(f)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    p = gauge(x)
    print(f"{p}")


def convert(f):
    x, y = f.split("/")
    if int(y) == 0: # should check for this ZeroDivisionError first since x > y will always be true for y = 0
        raise ZeroDivisionError
    elif x.isdigit() is False or y.isdigit() is False:
        raise ValueError
    elif int(x) > int(y):
        raise ValueError
    else:
        return round(int(x) / int(y) * 100)


def gauge(percent):
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()
