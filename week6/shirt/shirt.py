from sys import exit, argv
from PIL import Image, ImageOps


def main():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    else:
        if file_extension_check(1) != file_extension_check(2):
            exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        before = Image.open(argv[1])
    except FileNotFoundError:
        exit("Could not find the image file")
    else:
        size = shirt.size # it is a tuple (600, 600)
        before = ImageOps.fit(before, size) # resize and crop the input
        before.paste(shirt, box = (0, 0), mask = shirt) # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste
        before.save(argv[2], format=None) # saving the image


def file_extension_check(i):
    match endpart := argv[i][(argv[i].index('.')):].lower(): # find period symbol location and slice from there to the end and finally making it lowercase. ":=" is walrus operator an assignment expression
        case ".png" | ".jpg" | ".jpeg":
            return endpart
        case _:
            exit("Invalid output")


if __name__ == "__main__":
    main()