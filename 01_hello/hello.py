#!/usr/bin/env python3

"""
Tiny Python Projects
by Ken Youens-Clark

CHAPTER 1: How to write and test a Python program
PROGRAM: Hello World!
PURPOSE: Say hello

AUTHOR: Steven Partlow <profsfrink@gmail.com>
DATE STARTED: 19/06/2023
DATE FINISHED:
"""

import argparse  # Import the argparse module in to the program


def get_args():  # Defin get_args() method
    """Get the command-line arguments"""

    parseer = argparse.ArgumentParser(
        description="Say hello"
    )  # Setup our program to accept arguments,
    # the description is our help message

    # Make the first argument optional using either -n or --name
    # If no argument is provided the name will default to 'World'
    # # metavar=name is the name of the optional argument that will
    # appear in the usage message
    parseer.add_argument('-n',
                         '--name',
                         metavar='name',
                         default='World',
                         help='Name to greet')
    return parseer.parse_args()  # Return any parsed arguements


def main():  # Define main() function
    """ Main program code """

    args = get_args(
    )  # Execute get_args() method then store return values in args

    print(
        "Hello, " + args.name + "!"
    )  # Concatentate the name argument to this string
    # and output to the console


if __name__ == "__main__":
    main()
