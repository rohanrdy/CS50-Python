def main():
    text = input("Input: ")
    output = shorten(text)

    print(f"Output: {output}")

def shorten(word):
    output = ""
    for i in word:
        if i not in 'aeiouAEIOU':
            output += i
    return output

if __name__ == "__main__":
    main()