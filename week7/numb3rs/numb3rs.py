import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        if all(0 <= int(ip.group(i)) <= 255 for i in range(1,5)):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()