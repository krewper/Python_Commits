from collections import deque
myStack = deque()
myStack2 = deque()
myStack
myStack.append("Vienna")
myStack.append("Berlin")
myStack.append("Zurich")
deque(["Vienna" , "Berlin", "Zurich"])

myStack2
myStack.append("Python")
myStack.append("Perl")
myStack.append("Ruby")
deque(["Python", "Perl", "Ruby"])

for element in myStack:
    print(element)

print("\n")

for element in myStack2:
    print(element)
    
print("\n")

for char in "Iteration":
    print(char, end = " ")
    