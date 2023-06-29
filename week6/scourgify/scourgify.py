from sys import exit, argv
import csv


if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")
else:
    if argv[1][-4:] == ".csv" and argv[2][-4:] == ".csv":
        try:
            f = open(argv[1])
        except FileNotFoundError:
            exit(f"Could not read {argv[1]}")
        else:
            listofdict = []
            with f as file:
                reader = csv.DictReader(file)
                for row in reader:
                    x, y = row["name"].split(', ')
                    listofdict.append({"first": y, "last": x, "house": row["house"]})
            with open(argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for i in range(len(listofdict)):
                    writer.writerow({"first": listofdict[i]["first"], "last": listofdict[i]["last"], "house": listofdict[i]["house"]})
    else:
        exit("Not a CSV file")
