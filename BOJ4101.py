while True:
    f, s = map(int, input().split())
    if f == 0 and s == 0:
        break
    else:
        if f < s or f == s:
            print("No")
        else:
            print("Yes")