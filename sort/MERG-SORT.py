#!/usr/bin/env python


def MERGE(A, p, q, r):
    #print A
    L = A[p:q+1]
    R = A[q+1:r+1]
    n1 = len(L)
    n2 = len(R)

    #print p,  q, n1,':', L
    #print q+1,r, n2,":", R

    i=0
    j=0
    for k in range(p,r+1,1):
        if  L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1

        # i have reach end of L
        if i == n1:
            A[k+1:r+1]=R[j:n2+1]
            break
        if j == n2:
            A[k+1:r+1]=L[i:n1+1]
            break
    
    #print A[p:r+1]
    #print '-'*80

def MERGE_SORT(A, p, r):
    if p<r:
        q=int((p+r)/2)
        MERGE_SORT(A,p,q)
        MERGE_SORT(A,q+1,r)
        MERGE(A,p,q,r)


if __name__ == "__main__":
    A = [3, 7, 9, 2, 21, 10]
    MERGE_SORT(A, 0, len(A)-1)
    print str(A)
    raw_input('press any key...')
