#!/usr/bin/python3
#A program that opens a text file, counts, and  prints the number of characters in a file
fname = input('Enter the filename: ')
#tries to find the name of the file adn if no name of the file is found it returns error  and terminates the process
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
fhand = open(fname)
inp = fhand.read()
enx = len(inp)
print('There were', enx, 'characters in ', fname)

