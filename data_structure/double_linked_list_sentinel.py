#!/usr/bin/env python


class ListNode(object):
    def __init__(self, key, prev=0, next=0):
        self.key = key
        self.prev=prev
        self.next=next


class DoubleLinkedList(object):
    def __init__(self):
        self.nil = ListNode('NIL')
        self.nil.prev = self.nil
        self.nil.next = self.nil


    def List_Delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def List_Search(self, k):
        x = self.nil.next
        while x!=self.nil and x.key!=k:
            x = x.next
        return x

    def List_Insert(self, key):
        x = ListNode(key)
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil
        
    def List_Print(self):
        x = self.nil.next
        while x!=self.nil:
            print x.key, x.prev, x, x.next
            x = x.next

if __name__ == '__main__':
    l = DoubleLinkedList()
    for i in range(1, 10):
        l.List_Insert(i)

    l.List_Print()

    x =l.List_Search(2)
    #print x

    l.List_Delete(x)
    #l.List_Print()


    y = l.List_Search(2)
    print y.key

    raw_input('press any key...')

