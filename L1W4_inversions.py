# Uses python3
# Count the number of inversions of a given sequence
# Input:
# integer n,
# sequence a_0, a_1, ...,a_{n-1}
# Output:
# the number of inversions in the sequence

# Example:
# Input:
# 5
# 2 3 9 2 9
# Output:
# 2
# Explanation:
# Two inversions,  (a_1,a_3) and (a_2,a_3)

# Solution Methods:
# Modify merge_sort, merge


def MergeSort(A):
    n = len(A)
    if n == 1:
        return A
    
    m = n // 2
    
    B = MergeSort(A[:m])
    C = MergeSort(A[m:])
    
    A_sort = Merge(B, C)
    
    return A_sort


def Merge(B, C):
    D = []
    while (len(B) != 0) and (len(C) != 0):
        b = B[0]
        c = C[0]
        if b <= c:
            D.append(b)
            B.pop(0)
        else:
            D.append(c)
            C.pop(0)
    
    D.extend(B)
    D.extend(C)
    
    return D


def NumOfInver(A):
    n = len(A)
    if n < 2:
        return A, 0
    
    m = n // 2
    
    B, num_inv_p = NumOfInver(A[:m])
    C, num_inv_q = NumOfInver(A[m:])
    
    A_sort, num_paris = NumofInverMerge(B, C)
    
    return A_sort, num_inv_p + num_inv_q + num_paris


def NumofInverMerge(B, C):
    D = []
    num = 0
    while (len(B) != 0) and (len(C) != 0):
        b = B[0]
        c = C[0]
        if b <= c:
            D.append(b)
            B.pop(0)
        else:
            D.append(c)
            C.pop(0)
            num += len(B)
        
    D.extend(B)
    D.extend(C)
    
    return D, num      


n = int(input())
a = list(map(int, input().split()))
sort_a, num_inv_a = NumOfInver(a)
print(num_inv_a)
