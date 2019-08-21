#Implementing LifoQueue operations in a threaded environment
from queue import LifoQueue
myStack = LifoQueue()

myStack.put('a')
myStack.put('b')
myStack.put('c')

myStack
#<queue.LifoQueue object at 0x7f408885e2b0>

myStack.get()
myStack.get()
myStack.get()


myStack.get_nowait()