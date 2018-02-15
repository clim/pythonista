# Fahrenheit to Celsius is (F – 32) * 5/9 = C

import sys
import console
import clipboard
import webbrowser

fahrenheit = float(sys.argv[1])
celsius = (fahrenheit - 32) * 5/9

clipboard.set(str(fahrenheit) + '⁰ F = ' + str(round(celsius, 2)) + '⁰ C')
webbrowser.open('workflow://')