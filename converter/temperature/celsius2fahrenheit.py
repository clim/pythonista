# Celsius to Fahrenheit is (9/5 * C) + 32 = F

import sys
import console
import clipboard
import webbrowser

celsius = int(sys.argv[1])
fahrenheit = (9/5 * celsius) + 32

clipboard.set(str(fahrenheit))
webbrowser.open('workflow://')
