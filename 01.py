#!/usr/bin/python3.5

import os

# Tip Calculator

os.system('clear')

title = "Tip Calculator"
print(title + "\n" + (len(title))*"-" + "\n")

for i in range(0, 10001, 250):
    output = format((i/100), '.2f')
    tip = format(((i/100)*.15), '.2f')
    print (("${}".format((str(output)).zfill(2))) + " ==========> " + ("${}".format((str(tip)).zfill(2))))


