#!/usr/bin/python3
#code to open a file by the name mbox-short and make everything upper case
fhand = open('mbox-short.txt')
for ln in fhand:
    tx = ln.rstrip()
    print(tx.upper())
