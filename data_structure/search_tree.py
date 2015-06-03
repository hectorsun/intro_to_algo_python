#!/usr/bin/env python



class TreeNode(object):
    def __init__(self, key, p='NIL', left='NIL', right='NIL'):
        self.key = key
        self.p = p
        self.left = left
        self.right = right


class SearchTree(object):
    def __init__(self, A=[]):
        self.head = 'NIL'
        for a in A:
            self.TREE_INSERT(a)

    def TREE_MINIMUM(self, x='HEAD'):
        if x == 'HEAD':
            x = self.head
        if x == 'NIL':
            return x
        while x.left != 'NIL':
            x = x.left
        return x


    def TREE_MAXIMUM(self, x='HEAD'):
        if x ==  'HEAD':
            x = self.head
        if x == 'NIL':
            return x
        while x.right != 'NIL':
            x = x.right
        return x

    def INORDER_TREE_WALK(self, x):
        if x != 'NIL':
            self.INORDER_TREE_WALK(x.left)
            print x.key
            self.INORDER_TREE_WALK(x.right)

    def INORDER_TREE_WALK2(self):
        pass

    def TREE_SEARCH(self,x, k):
        if x == 'NIL' or k==x.key:
            return x
        if k<x.key:
            return self.TREE_SEARCH(x.left, k)
        else:
            return self.TREE_SEARCH(x.right, k)

    def TREE_INSERT(self, key):
        z = TreeNode(key, 'NIL', 'NIL', 'NIL')
        y = 'NIL'
        x = self.head
        while x != 'NIL':
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == 'NIL':
            self.head = z
        elif z.key <y.key:
            y.left = z
        else:
            y.right = z
    
    def TRANSPLANT(self, u, v):
        if u.p == 'NIL':
            self.head = v
        elif u == u.p.left:
            u.p.left = v
        else:#u == u.p.right
            u.p.right = v

        if v != 'NIL':
            v.p = u.p


    def TREE_DELETE(self, z):
        if z.left == 'NIL':
            self.TRANSPLANT(z, z.right)
        elif z.right == 'NIL':
            self.TRANSPLANT(z, z.left)
        else:
            y = self.TREE_MINIMUM(z.right)
            if y.p != z:
                self.TRANSPLANT(y, y.right)
                y.right = x.right
                y.right.p = y
            self.TRANSPLANT(z, y)
            y.left = z.left
            y.left.p = y

if __name__ == '__main__':
    T = SearchTree([i for i in range(0,11)])
    

    #print 'minimum  = ',T.TREE_MINIMUM().key
    
    #x = T.TREE_SEARCH(T.head, 2)
    #T.TREE_DELETE(x)

    T.INORDER_TREE_WALK(T.head)

    raw_input('press any key...')
