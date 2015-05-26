#!/usr/bin/env python

#definition of heap
class heap(object):
        def __init__(self, data = [], size = 0):
                self.data = data
                self.heapSize = size

        def setHeapSize(self, size):
                self.heapSize = size
        def getHeapSize(self):
                return self.heapSize

	def __len__(self):
		return len(self.data)
	def __getitem__(self, key):
		return self.data[key]
	def __setitem__(self, key, value):
		self.data[key] = value
        def exchangeData(self, i1, i2):
                buf = self.data[i1]
                self.data[i1] = self.data[i2]
                self.data[i2] = buf

        # print the heap in tree style
        def printHeap(self):
                print self.data
                
      
# parent node and child node
def PARENT(i):
        return int(i/2)
def LEFT(i):
        return 2*i
def RIGHT(i):
        return 2*i+1



# keep a heap to be max heap
# A : a heap
# i : a index, whose left sub tree and right sub these both are max heap
def MAX_HEAPIFY(H, i):
	l = LEFT(i)
	r = RIGHT(i)
	if l<H.getHeapSize() and H[l]>H[i]:
		largest = l
	else:
		largest = i

	if r<H.getHeapSize() and H[r]>H[largest]:
		largest=r
	if largest != i:
                H.exchangeData(largest, i)
		MAX_HEAPIFY(H, largest)
		


#translate a array to a max heap
def BUILD_MAX_HEAP(H):
        H.setHeapSize(len(H))
	for i in range( int(len(H)/2), 0-1, -1):
                MAX_HEAPIFY(H, i)

# main function of heap sort
def HEAPSORT(H):
        # translte h into a max heap
        BUILD_MAX_HEAP(H)
        # 
        for i in range(len(H)-1, 1-1, -1):
                # exchange data in H[i] and H[1]
                H.exchangeData(0, i)

                H.setHeapSize(H.getHeapSize()-1)
                MAX_HEAPIFY(H,0)

if __name__ == "__main__":
        # raw data
        A = [3, 4, 2, 8, 5 , 9, 1, 10, 16, 20, 27, 6, 7]
        H = heap(A, len(A))
        
        H.printHeap()
        
        HEAPSORT(H)

        print '-'*80
        H.printHeap()

        raw_input("press any key...")
