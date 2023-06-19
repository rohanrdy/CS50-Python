list = []

while True:
    try:
        items = input().upper()
    except EOFError:
        print("")
        break
    else:
        list.append(items)

list.sort()

k = 0

for i in list:
    count = 0
    if k==0 or list[k] != list[k-1]:
        if list[k] != list[-1]:
            l = k
            while list[l] == list[l+1]:
                count += 1
                l +=1
        elif len(list) == 2 and list[k] == list[k-1]:
            count += 1
        print(count+1, i)

    k += 1