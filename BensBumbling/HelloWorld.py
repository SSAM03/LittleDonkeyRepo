#! /usr/bin/python
# script to take an argument and turn it into something

import sys

if len(sys.argv)==1:
    print "Please enter your name on the command line as a parameter to the script, for instance python HelloWorld.py ben"
else:
    arg = sys.argv[1]
    print "Your name is", arg
    print "The name", arg, "has", len(arg), "letters in it"
    print arg, "backwards is", arg[::-1]

#Hi Ben missing parentheses for the print statement, so it #doesn't work on python 3.X interpreters
#get Anaconda from https://www.anaconda.com/download/