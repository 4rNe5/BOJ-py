input = int(input())

for i in range(input,0,-1):
    blank = i - 1
    print(" " * (blank),end="")
    for star in range(input - blank):
        print("*",end="")
    print()