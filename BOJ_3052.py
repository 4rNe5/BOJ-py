l1 = set()

for i in range(10):
    n = int(input())
    l1.add(n % 42)

print(len(l1))
