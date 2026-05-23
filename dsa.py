# n = int(input("enter the no:- "))
# x = []
# for i in range(1, n+1):
    
#     if i % 3 == 0 and i % 5 == 0:
#         x.append( "fizzbuzz")
#     elif i % 3 == 0:
#         x.append("fizz")    
#     elif i % 5 == 0:
#         x.append("buzz")
#     else:
#         x.append(str(i))
# print(x)



# low = int(input("enter a no. - "))
# high = int(input("enter a no. - "))

# x = []
# for i in range(low, high +1):
#     if i%2 != 0:
    
#         x.append(i)    
# print('the odd numbers btw', low, 'and', high, 'are', x)

# x = []
# count = 0
# for i in x:

#     for j in x:
#         if j<i:
#             count =+1
# print(x)

# class Solution:
#     def countDigit(self, num: int) -> int:

# n = 51286

# while n>0:
#     r = n%10
#     print(r,end = " ")
#     n = n // 10 

#find palindrom no.

# x = int(input('enter a no.- '))
# temp = x
# rev=0
# while temp>0:
#     r=temp%10
#     temp //= 10
#     rev=rev*10 +r
# print(rev)
# print(temp)

# class solution:
#     def ispalindrome(self, x: int):
#         temp = x
#         rev = 0
#         while temp>0:
#             r = temp%10
#             rev = rev*10 + r
#         return rev==x

# x = int(input('enter the no:-'))
# temp = x
# product = 1
# sum = 0
# while temp>0:
#     r=temp%10
#     temp//=10
#     product = product * r
#     sum = sum + r 
# print(x)
# print(product)
# print(sum)
# print(product-sum)

# class solution:
#     def cal(self, x : int):
#         temp =x
#         product =1
#         sum = 0
#         while temp>0:
#             r= temp%10
#             temp//=10
#             product = product * r
#             sum = sum + r
#         return product-sum//

#recurssion with loop
# n= 5
# i= 1
# while i<=5:
#     print(i,end=" ") 
#     i+=1
#recussion with function
# def printNumber(i,n):
#     if i>n:
#         return
#     print(i,end=" ")
#     printNumber(i+1,n)
# printNumber(1,5)

# def factorial(x):
   
#     if(x == 0 or x == 1):
#         return 1
#     else:
#         return  x * factorial(x-1) 
# num=int(input('eneter the no:- '))
# a = factorial(num)
# print(a)

# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n,end=" ")
    
# fun (6) 

#find nth fibonai no
# def fib(n):
#     #base cae
#     if(n==0):
#         return 0
#     elif (n==1):
#         return 1
#     #recussive 
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(3))   
# print(fib(12))   
# print(fib(10))

# arryas 1-d
# import numpy as np
# list1 = [10,20,30,40]
# array1= np.array(list1)
# print(array1)
# print(type(array1))

# #arryas 2-d
# import numpy as np
# list1 = [[10,20,30,40] ,[55,44,66,77],[2,3,4,5]]
# arr = np.array(list1)
# print(arr)
# print(type(arr))


import numpy as np
# arr= np.arange(11,17).reshape(2,3)
# print(arr)

#zeros
# arr = np.zeros((4,2))
# print(arr)
# arr = np.ones((4,2))
# print(arr)

# list = [1,2,3,4,5,6,8,9,7]
# list = [[10,20,30,40] ,[55,44,66,77],[2,3,4,5]]
# arr = np.array(list)
# print(arr.ndim)
# print(arr.size)
# print(arr.shape)
# print(arr.dtype)
# print(arr.itemsize)

# arr=np.array([10,20,30,40,50])
# print(arr, type(arr))

# arr1=np.array([[10,20,30,40,50],[100,200,300,400,500],[1000,2000,3000,4000,5000]])
# print(arr1, type(arr1))

#slicing
# arr = np.array([10,20,30,40,50,60])
# print(arr)
# print(arr[1])
# print(arr[1:6:2])
# print(arr[::2])
# print(arr[::-1])
# print(arr[-1])
# print(arr[:-1:])
# print(arr[-1:-3:-1])

# x= np.array([[1,2],[3,4]])
# y= np.array([[11,22],[33,44]])
# z= x+y
# print(z)
# print(x-y)
# print(x*y)
# print(x@y)
# print(y / x)
# print(y // x)
# print(y % x)
# print(y** x)
# print(x.transpose())


#pandas 
# import pandas as pd
# df = pd.read_excel(r"Book1.xlsx")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.values)
# print(df.index)
# print(df.size)

# print(df.iloc[[0,2,4]])

#create data frame
# data = {'name' : ['chirag', 'sam', 'man','son'],
#     'age' : [20,63,53,39],
#     'addres' : ['vijay', 'nzm', 'ndls','sectore 83']
# }
# df=pd.DataFrame(data)
# print(df)

#linklist

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# current = node1
# while current is not None:
#     print(current.data, end="-> ")
#     current=current.next
# print("none")

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
new_node=Node(50)
new_node.next = head
head = new_node 

# current = new_node
# while current is not None:
#     print(current.data, end='-> ')
#     current= current.next
# print('none')
 
# #deleting head node
# if head is not None:
#     head = head.next

# current = head
# while current is not None:
#     print(current.data, end='-> ')
#     current = current.next
# print('none')

# #dlelting form last node

# current =head
# while current.next is not None :
#     print(current.data , end='-> ')
#     current = current.next
# current.next = None
# print('none')

#deleting particualr node

current = head
while current.next.data !=20:
    print(current.data, end='-> ')
    current=current.next
current.next =current.next.next
print("none")
