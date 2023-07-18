import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if x := re.search(r"^(1?\d)(:[0-5]\d)? (AM|PM) to (1?\d)(:[0-5]\d)? (AM|PM)$", s):
        if x.group(3) == "AM" and x.group(6) == "PM":
            if 0 < int(x.group(1)) < 13 and 0 < int(x.group(4)) < 13:
                p = x.group(2)
                q = x.group(5)
                if not p: p = ":00"
                if not q: q = ":00"
                if (x.group(1) and x.group(4)) == "12":
                    return f"00{p} to {x.group(4)}{q}"
                return f"{x.group(1).zfill(2)}{p} to {int(x.group(4))+12}{q}"
            pass
        elif x.group(3) == "PM" and x.group(6) == "AM":
            if 0 < int(x.group(1)) < 13 and 0 < int(x.group(4)) < 13:
                p = x.group(2)
                q = x.group(5)
                if not p: p = ":00"
                if not q: q = ":00"
                return f"{int(x.group(1))+12}{p} to {x.group(4).zfill(2)}{q}"
            pass
        raise ValueError("lol")
    else:
        raise ValueError("lol")


if __name__ == "__main__":
    main()