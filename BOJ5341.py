while True:
    p = int(input())
    cnt = 0
    if p == 0:
        break
    else:
        for i in range(p,0,-1):
            cnt = cnt + i
        print(cnt)