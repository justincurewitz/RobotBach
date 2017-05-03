from __future__ import print_function
f = open('../30000 epochs/data.txt', 'r')
w = open('../30000 epochs/error.csv', 'w')

print("epoch, error", file=w)
for line in f:
    if 'epoch' in line:
        words = line.split()
        error = words[2].split("=")[1]
        new_line = words[1]+" "+ error
        print(new_line, file=w)
