#!python3

# Fahrenheit to Celsius is (F – 32) * 5/9 = C

import sys
import console
import clipboard
import webbrowser

fahrenheit = float(sys.argv[1])
celsius = (fahrenheit - 32) * 5/9

clipboard.set("{0:.1f}⁰ F = {1:.1f}⁰ C".format(fahrenheit, celsius))
webbrowser.open('workflow://')
