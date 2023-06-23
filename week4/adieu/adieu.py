names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        names.append(name)

initial = "Adieu, adieu, to"

for i in range(len(names)):
    if i == 0:
        print(initial, names[i], end = "")
    elif names[i] != names[-1]:
        print(", " + names[i], end = "")
    else:
        print(" and " + names[i], end = "")