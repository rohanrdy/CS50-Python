while True:
    f = input("Fraction: ")
    f = f.split("/")
    try:
        f[0] = int(f[0]) # if f[0] cannot be converted to an integer then ValueError will be raised
        f[1] = int(f[1])
#       if f[1]==0:
#          raise ZeroDivisonError
        percent = (f[0]/f[1])*100 # we can use line 7 and 8 (and move percent calculation after the while loop) or this. If f[1] is zero then ZeroDivisionError will be raised
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if f[0] <= f[1]:
            break

if percent >= 99:
    print("F")
elif percent <= 1:
    print("E")
else:
    print(f"{percent:.0f}%")