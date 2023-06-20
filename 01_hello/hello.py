#!/usr/bin/env python3

# Tiny Python Projects
# by Ken Youens-Clark

# CHAPTER 1: How to write and test a Python program

# AUTHOR: Steven Partlow
# DATE STARTED: 19/06/202
# DATE FINISHED: 

# ----------------------------------------------------------------------------------------------------------------------

# Purpose: Say hello

import argparse # Import the argparse module in to the program

parseer = argparse.ArgumentParser(description='Say hello') # Setup our program to accept arguments, the description is our help message

# Make the first argument optional using either -n or --name
# If no argument is provided the name will default to 'World'
# # metavar=name is the name of the optional argument that will appear in the usage message
parseer.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')

args = parseer.parse_args() # Take an arguments passed into the program parse them 

print('Hello, ' + args.name + '!') # Concatentate the name argument to this string and output to the console
