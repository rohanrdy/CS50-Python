menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cost = 0

while True:
    try:
        food =input("Input: ").strip().lower().title()
        if food not in menu:
            raise KeyError
    except KeyError:
        continue
    except EOFError:
        print("")
        break
    else:
        cost += menu[food]
        print(f"Total: ${cost:.2f}")