#!/usr/bin/env python



# find out maximum and minimum in a array
# With this algorithm, only (3*int(len(A)/2)) times of comparaion are necessary.
def MAX_MIN(A):
    # find out maximum and minimum of 2 numbers
    def MAX_MIN_IN_2(n1, n2):
        if n1>n2:
            return n1,n2
        else:
            return n2,n1

    n = len(A)
    if n%2 == 0 :#even
        max,min = MAX_MIN_IN_2(A[0], A[1])
        start = 2
    else: # odd
        max = min = A[0]
        start = 1


    for i in range(start, n, 2):
        max_in_2, min_in_2 = MAX_MIN_IN_2(A[i], A[i+1])
        
        if min_in_2 < min:
            min = min_in_2

        if max_in_2 > max:
            max = max_in_2

    return max, min
            

if __name__ == '__main__':
    A = [9, 2, 10, 7, 20, 8, 13, 17, 30, 1]
    print MAX_MIN(A)
