import re

fh = open('mbox-short.txt')
for line in fh:
    line = line.rstrip()
    if re.search('^from: ', line):
        print(line)
