# Little Helper to convert txt to csv
# ***********************************************
# Put all files to convert into the input folder
# Run script
# Find the output fildes in the output folder
# ***********************************************
# Author: Sebastian Schweiger
# Date: 22.01.2019
# Last Update: 10.02.2019
# Version 1.0
# ***********************************************


import pandas as pd
import glob
import os


def choose_delimiter():
    """Get user input about what the delimiter of the input files is and return it."""
    return input("Please enter the delimiter of the input files:\n")


def choose_separator():
    """Get user input if the user wants to choose the seperatorself.
    I "y/Y" (yes) get input what tehe separator should be and return itself.
    Else return standard value (';')."""
    choice = input(
        "Do you want to change the separator for the output files (not recommended)? (y/n)\n")
    if choice.lower() == "y":
        return input("Please enter the separator for the output files\n(; is recommended):\n")
    else:
        return ';'


def process_files(delimiter, separator):
    """Process all files in subfolder './input' by replacing the chosen delimiter with the chosen separator
    and convert the .txt to a .csv and save it in subfolder './output'."""
    os.chdir("./input")

    for file in glob.glob("*.txt"):
        df = pd.read_fwf(file, delimiter=delimiter)
        df.to_csv("..\\output\\"+file[:-4]+".csv", sep=separator, index=False)
        print(file)


delimiter = choose_delimiter()
separator = choose_separator()
print()
process_files(delimiter, separator)
