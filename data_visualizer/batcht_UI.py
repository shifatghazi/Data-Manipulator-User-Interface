# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Michael Aziz"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101282918"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-115"

#==========================================#
# Place your script for your batch_UI after this line

import numpy as np
import matplotlib.pyplot as plt
import sort
import load_data
import histogram
import curve_fit


filename = input(
    "Please enter the name of the file where your commands are stored: ")

with open(filename, 'r') as f:
    commands = f.readlines()


for command in commands:

    args = command.strip().split(';')

    command_type = args[0]

    if command_type == 'L':
        filename = args[1]
        data = load_data.load_data(filename, (args[2], args[3]))
        print("Data loaded")
    elif command_type == 'S':
        column = args[1]
        order = args[2]
        data = sort.sort(data, order, column)
        print("Data sorted. <<<You selected not to display>>>")
        if args[3] == "Y":
            print(data)
    elif command_type == 'H':
        column = args[1]
        histogram.histogram(data, column)
        print("<<<Histograms with Study time will be shown>>>".format(column))

        
        
        



