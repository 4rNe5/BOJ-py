x,y = map(int, input().split())

if x > 0 & y > 0:
    print(1)
elif x < 0 & y > 0:
    print(2)
elif x < 0 & y < 0:
    print(3)
elif x > 0 & y < 0:
    print(4)
