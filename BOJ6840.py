a = []
for i in range(0,3,1):
    a.append(int(input()))
a.remove(max(a))
a.remove(min(a))
print(a[0])