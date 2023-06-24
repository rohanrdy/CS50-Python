import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        names.append(name)

print(f"Adieu, adieu, to {p.join(names)}")

"""
# code works but check50 is not accepting. In the hint it suggests to use inflect module with which it works.

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
"""