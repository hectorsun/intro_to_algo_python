#!/usr/bin/env python

# counting sort algorithm
# A: the array to sorted
# k: all elements in A are in the range of 0 and  k
# note : reslut will be returned as result of function
def COUNTING_SORT(A, k):
    C = [0]*(k+1)
    for j in range(0, len(A)):
        C[A[j]]+=1
    #C[i] contains the number of element equal to i
    

    for i in range(1, k+1):
        C[i]+=C[i-1]

    B = [0]*len(A)
    for j in range(len(A)-1, 0-1, -1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]-=1

    return B
    





if __name__ == "__main__":
    A = [19, 1, 7, 6, 4, 2, 5, 3, 9]
    print A
    B = COUNTING_SORT(A, 21)
    print B
    raw_input("press any key...")
