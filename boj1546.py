s = int(input())
fs = 0
score = list(map(int, input().split()))
for i in range(0,s,1):
    fs = fs + (score[i]/max(score)*100)
print(fs/s)