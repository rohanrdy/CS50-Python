from sys import exit, argv
import csv
import tabulate


if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) == 2:
    file_path = argv[1]
else:
    exit("Too many command-line arguments")

if file_path[-4:] == ".csv":
    try:
        f = open(file_path)
    except FileNotFoundError:
        exit("File does not exist")
    else:
        menu_list = []
        with f as file:
            reader = csv.reader(file)
            for row in reader:
                menu_list.append(row)
        print(tabulate.tabulate(menu_list, headers="firstrow", tablefmt="grid"))
else:
    exit("Not a CSV file")
