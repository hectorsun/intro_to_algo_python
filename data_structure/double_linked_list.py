#!/usr/bin/env python

class ListNode(object):
    def __init__(self,key,  next=0, prev=0):
        self.next = next
        self.prev = prev
        self.key = key


class DoubleLinkedList(object):
    def __init__(self):
        self.head = 0

    # search a node whose data is k in the list
    def List_Search(self, k):
        x = self.head
        while x != 0 and x.key != k:
            x = x.next
        return x

    # insert a nod whose data is key into head of list
    def List_Insert(self, key):
        x = ListNode(key)
        x.next = self.head
        if self.head != 0:
            self.head.prev = x
        self.head = x
        x.prev = 0

    def List_Delete(self, x):
        if x. prev != 0:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != 0:
            x.next.prev = x.prev
        

if __name__ == "__main__":
    l = DoubleLinkedList()

    # insert [0...9] into the list
    for i in range(0, 10):
        l.List_Insert(i)

    # search node whose data is 2 in the list
    x = l.List_Search(2)
    if x!=0:
        print "node is found, and it's key is ", str(x.key)
    else:
        print "node cannot be found"

    # delete the node whose data is 2
    l.List_Delete(x)

    # search the node again
    print l.List_Search(2)

    raw_input('press any key...')
