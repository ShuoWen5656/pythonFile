# 全局变量，作为邮差
import collections



# dq队列作为变量传递
def initDq():
    global dq
    dq = collections.deque()


def pop():
    return dq.pop()


def append(a):
    try:
        dq.index(a)
    except:
        dq.append(a)


def size():
    return dq.__len__()

def get(index):
    return dq.__getitem__(index)

def remove(e):
    try:
        dq.remove(e)
    except:
        return

def printList():
    for i in dq:
        print(i)

if __name__ == '__main__':
    initDq()
    append("123")
    append("345")
    printList()

