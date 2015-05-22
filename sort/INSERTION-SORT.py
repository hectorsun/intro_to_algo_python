##!/usr/bin/env python

def INSERTION_SORT(A):
        "INSERTION_SORT"
        for j in range(1, len(A)-1):
                key = A[j]
                i = j-1
                while i>=0 and A[i]>key:
                        A[i+1] = A[i]
                        i-=1
                A[i+1]=key
        return A






if __name__ == "__main__":
        print __name__
        A=[2, 5, 1, 8, 10]
        print "Before:" + str(A)
        B = INSERTION_SORT(A)
        print "After: "+ str(B)
        raw_input("press any keyy...")
