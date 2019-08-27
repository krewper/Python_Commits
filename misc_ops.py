#swapping variables in-place
x, y = 10, 20
print(x, y)

x, y = y, x
print(x, y)

#Reversing a string
a = "Kongsberg Digital India"
print("Reverse is", a[::-1])

#Creating a single string from all the elements in a list
a = ["Geeks", "For", "Geeks"]
print(" ".join(a))

#chaining of comparision operators
n = 10
result = 1 < n <20
print(result)
result = 1>n <=9
print(result)

#printing file paths of imported modules
import numpy;
import requests;

print(numpy)
print(requests)

#using enums in python
class MyName:
    Geeks, For, Geeks = range(3)
print(MyName.Geeks)
print(MyName.For)
print(MyName.Geeks)

#returning multiple values from a single function
def r():
    return 1, 2, 3, 4
a, b, c, d = r()

print(a, b, c, d)


#finding the most frequent value in a list
test = [1, 2, 3, 4, 2, 2, 3, 2, 4, 1, 4, 4]
print(max(set(test), key = test.count))

#check the memory usage of an object
import sys
x = 1
print(sys.getsizeof(x))

#print string n times
n = 2;
a = "GeeksforGeeks";
print(a * n);

#checking if two words are anagrams
from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
print(is_anagram('geek', 'eegk'))
print(is_anagram('geek', 'peek'))