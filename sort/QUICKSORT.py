#!/usr/bin/env python

def exchange(A, i1, i2):
    buf = A[i1]
    A[i1] = A[i2]
    A[i2] = buf


def PARTITION(A, p, r):
    #x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= A[r]:
            i+=1
            exchange(A, i, j)
    exchange(A, i+1, r)
    return i+1




def QUICKSORT(A, p, r):
    if p<r:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q-1)
        QUICKSORT(A, q+1, r)


if __name__ == '__main__':
    #A = [8, 6 , 12, 20, 17, 10, 4, 15, 1]
    A = [8, 7, 6,5,4,3,2,1,0]
    print str(A)
    QUICKSORT(A, 0, len(A)-1)
    print str(A)
