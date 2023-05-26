N, M = map(int, input().split())

A = [[0 for i in range(M)] for j in range(N)]
B = [[0 for i in range(M)] for j in range(N)]

for i in range(0, N):
	A[i] = list(map(int, input().split()))

for i in range(0, N):
	B[i] = list(map(int, input().split()))

for i in range(0, N):
	for j in range(0, M):
		A[i][j] += B[i][j]
		print(A[i][j], end = " ")
	print()