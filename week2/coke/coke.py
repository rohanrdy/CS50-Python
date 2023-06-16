due = 50

while True:
    print("Amount Due:", due)
    money = int(input("Insert Coin: "))
    if money == 25 or money == 10 or money == 5:
        if(money >= due):
            print("Change Owed:", money-due)
            break
        due -= money
    else:
        continue