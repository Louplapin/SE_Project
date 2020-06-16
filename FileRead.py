import sys

f = open(sys.argv[1], 'r')
list = f.readlines()
for line in list:
    print(line)
f.close()