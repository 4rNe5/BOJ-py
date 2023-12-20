rge = int(input())
number = int(input())
cnt = 0

a = []
while(number!=0):
    a.append(number%10)
    number = number//10

print(sum(a))