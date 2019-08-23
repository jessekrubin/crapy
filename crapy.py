import sys

def print(string):
    for c in string:
        sys.stdout.write(c)
    sys.stdout.write('\n')

def add(a, b):
    total = 0
    for i in range(a+1):
        for j in range(b+1):
            total += 1
    return total

