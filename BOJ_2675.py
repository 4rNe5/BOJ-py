r = int(input())

for _ in range(0,r,1):
    num, word = map(str, input().split())
    num = int(num)
    for i in word:
        print(i*num, end = "")
    print()