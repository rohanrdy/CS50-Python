def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if time.endswith(" a.m."):
        time = time.split(' a.m.')
        time = time[0].split(':')
        return round(int(time[0]) + int(time[1])/60, 2)
    elif time.endswith(" p.m."):
        time = time.split(' p.m.')
        time = time[0].split(':')
        return round(12 + int(time[0]) + int(time[1])/60, 2)
    else:
        time = time.split(":")
        return round(int(time[0]) + int(time[1])/60, 2)

if __name__ == "__main__":
    main()