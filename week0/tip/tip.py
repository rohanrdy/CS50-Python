def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.strip('$')
    d = float(d)
#   d = round(d, 2)
    return d

def percent_to_float(p):
    p = p.strip('%')
    p = float(p)/100
#   p = round(p, 2)
    return p

main()