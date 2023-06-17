def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[0:2].isalpha() and 1<len(s)<7 and s.isalnum() and no_middle_num(s):
        return True

def no_middle_num(s):
    temp = 0
    for i in range(3): # checking from the last to see if any number comes before an alphabet
        if s[(len(s)-1)-i].isalpha():
            if s[(len(s)-i-1)-1].isnumeric():
                temp+=1
    if temp > 0: # means that numbers came in the middle of the plate
        return False
    if temp == 0: # to check if the first number is a zero
        for j in range(len(s)-1):
            if s[j].isalpha():
                if s[j+1] == "0":
                    return False
    return True

main()
