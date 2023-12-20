A = [15,36,65,15,22,53,7]

def quick_sort(A, left, right):
    if left < right:
        i = left + 1
        j = right
        pivot = A[left]
        while i <= j :
            while i <= right and A[i] <= pivot : i += 1
            while i >= left and A[j] > pivot : j -= 1
            if i < j: A[i], A[j] = A[j], A[i]
            print_qs(A)
        A[left], A[j] = A[j], A[left]
        print_qs(A)
        quick_sort(A, left, j-1)
        quick_sort(A, j+1, right)
s = 1
def print_qs(A):
    global s
    print("Step",s,"=",A)
    s += 1
quick_sort(A,0,6)