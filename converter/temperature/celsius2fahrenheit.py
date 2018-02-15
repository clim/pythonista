# Celsius to Fahrenheit is (9/5 * C) + 32 = F

import sys
import console
import clipboard
import webbrowser

celsius = float(sys.argv[1])
fahrenheit = (9/5 * celsius) + 32

clipboard.set(str(celsius) + '⁰ C = ' + str(round(fahrenheit, 1)) + '⁰ F')
webbrowser.open('workflow://')