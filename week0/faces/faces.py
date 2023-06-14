def main():
    text = input("Enter the text : ")
    text = convert(text)
    print(text)

def convert(x):
    x = x.replace(":)", "🙂").replace(":(", "🙁")
    return x

main()