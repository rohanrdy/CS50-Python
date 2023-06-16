def main():
    text = input("Input: ")
    output = ""

    for i in text:
        if isnotvowel(i):
            output += i

    print(f"Output: {output}")

def isnotvowel(n):
    if n not in 'aeiouAEIOU':
        return True

main()