cnt = int(input())

for i in range(cnt):
    H, W, N = map(int, input().split())
    ccnt = 1
    while N > H:
        N = N - H
        ccnt += 1
    print(N * 100 + ccnt)