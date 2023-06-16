text = input("camelCase: ")
output = ""

for char in text:
    if char.isupper():
        output += '_' + char.lower()
    else:
        output += char
print("snake_case:", output)