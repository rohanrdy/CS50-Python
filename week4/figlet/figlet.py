from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet() #for some reason directly using Figlet() is not working..should use a variable like figlet
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    random_font = choice(font_list)
    figlet.setFont(font=random_font)

elif len(sys.argv) == 3:
    specific_font = sys.argv[2]
    if sys.argv[1] == '-f' or sys.argv[1] == '--font' and specific_font in font_list:
        figlet.setFont(font=specific_font)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print("Ouput:", figlet.renderText(text), sep="\n")