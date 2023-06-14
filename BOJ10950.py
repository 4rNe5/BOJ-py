def plus(a,b):
    return a+b

for i in range(0,int(input()),1):
    a, b = map(int, input().split())
    print(plus(a,b))
