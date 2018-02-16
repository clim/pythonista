#!python3

# Celsius to Fahrenheit is (9/5 * C) + 32 = F

import sys
import console
import clipboard
import webbrowser

celsius = float(sys.argv[1])
fahrenheit = (9/5 * celsius) + 32

clipboard.set("{0:.1f}⁰ C = {1:.1f}⁰ F".format(celsius, fahrenheit))
webbrowser.open('workflow://')
