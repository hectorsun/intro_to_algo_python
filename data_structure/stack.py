#!/usr/bin/env python


class STACK(object):
    def __init__(self, num=10):
        self.num = num
        self.data = [0 for x in range(0, self.num)]
        self.top = -1

    def STACK_EMPTY(self):
        if self.top == -1:
            return True
        else:
            return False

    def PUSH(self, x):
        if self.top == self.num-1:
            raise Exception('overflow')
        self.top+=1
        self.data[self.top] = x

    def POP(self):
        if self.STACK_EMPTY()==True:
            raise Exception("underflow")
        else:
            self.top-=1
            return self.data[self.top+1]


if __name__ == '__main__':
    s = STACK()
    print s.STACK_EMPTY()
    
    for i in range(0, 10):
        s.PUSH(i)

    print s.STACK_EMPTY()


    for i in range(0, 10):
        print s.POP()


    raw_input('press any key...')

