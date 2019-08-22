from collections import deque
myStack = deque()
myStack2 = deque()

#function myFunc returns the length of the Stack
def myFunc(e):
  print (len(e))


myStack.append('a')
myStack.append('b')
myStack.append('c')
myFunc(myStack)

myStack
deque(['a' ,'b' ,'c'])

myStack2
deque(['a' ,'b' ,'c'])


