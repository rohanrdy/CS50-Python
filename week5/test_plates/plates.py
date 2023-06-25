def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and 1 < len(s) < 7 and s.isalnum():
        temp = 0
        flag = 1
        firstzero = 0
        if len(s) > 3:
            for i in range(
                3
            ):  # checking from the last to see if any number comes before an alphabet
                if s[(len(s) - 1) - i].isalpha():
                    if s[(len(s) - i - 1) - 1].isnumeric():
                        temp += 1
            if temp > 0:  # means that numbers came in the middle of the plate
                flag = 0
        else:
            temp = 0
        if temp == 0:  # to check if the first number is a zero
            for j in range(len(s) - 1):
                if s[j].isalpha():
                    if s[j + 1] == "0":
                        firstzero = 1
        if flag == 1 and firstzero == 0:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
