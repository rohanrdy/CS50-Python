import random

def main():
    level = get_level()
    error = 0
    score = 0
    for _ in range(0, 10):
        X = generate_integer(level)
        Y = generate_integer(level)
        while True:
            try:
                temp = int(input(f"{X} + {Y} = "))
                break
            except ValueError:
                print("EEE")
                error += 1
                break
        if temp != X+Y:
            print("EEE")
            while True:
                try:
                    temp = int(input(f"{X} + {Y} = "))
                except ValueError:
                    print("EEE")
                    error += 1
                    break
                else:
                    if temp == X+Y:
                        score += 1
                        break
                    error += 1
                    print("EEE")
                    if error == 2:
                        print(f"{X} + {Y} = {X+Y}")
                        error = 0
                        break
        else:
            score += 1
    print("Score:", score)

def get_level():
    while True:
        try:
            l = int(input("Level: "))
        except ValueError:
            pass
        else:
            if l == 1 or l == 2 or l == 3:
                return l
            else:
                pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return (random.randint(100, 999))

if __name__ == "__main__":
    main()

"""
def main():
    n_attempts = 0
    wrong_answers = 0
    score = 0

    level = get_level()

    while n_attempts < 10:
        if wrong_answers == 0:
            x = generate_integer(level)
            y = generate_integer(level)

            right_answer = x + y

        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            wrong_answers += 1
        else:
            if answer == right_answer:
                n_attempts += 1
                if wrong_answers == 0:
                    score += 1

                wrong_answers = 0
            elif wrong_answers < 3:
                print("EEE")
                wrong_answers += 1

        if wrong_answers == 3:
            print(f"{x} + {y} = {right_answer}")
            wrong_answers = 0
            n_attempts += 1

    print(f"Score: {score}")
"""