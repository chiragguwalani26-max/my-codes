# x = [1, 5, 8, 6, 3]
# x.sort()
# print(x) 

#bubble sort

# x=[1,5,7,4,6,8,2,6,3,4,2,6,1]
# print(x)
# n= len(x)
# for i in range(n):
#     for j in range(n-i-1):
#         if x[j] > x[j+1]:
#             #swap
#             y = x[j]
#             x[j] = x[j+1]
#             x[j+1] = y
# print(x)


#insertion sort
# x= [1,5,2,6,3,4,2,9,8,7,4]
# print(x)
# n= len(x)

# for i in range(1,n):
#     key = x[i]
#     j = i - 1
#     while j>=0 and x[j]>key:
#         x[j+1]=x[j]
#         j-=1
#     x[j+1] = key  

# print(x)


#selection sort

# def selection(arr):
#      n= len(arr)
#      for i in range(n-1):
#           mini = i
#           for j in range(i+1,n):
#                if arr[j]< arr[mini]:
#                     mini=j
#                     arr[i],arr[mini]= arr[mini],arr[i]
# arr = [24,41,33,42,17]
# selection(arr)
# print(arr)

#serching
#linear search

# n= [2,5,3,9,2,10,30,20,59]
# tar = 0
# def liner( n, tar):
#     for i in range(len(n)):
#         if n[i]==20:
#             return i
#     return - 1
# print(liner(n,20))

#binary search
# n= [10,20,30,40,50,60,70]
# tar = 0
# def binary(n, tar):
#     left,right = 0,len(n)-1
#     while left<=right:
#         mini = (left+right)//2
#         if n[mini] == tar:
#             return mini
#         elif n[mini]<tar:
#             left = mini + 1 
#         else:
#             right = mini - 1 
#     return -1
# print(binary(n,70))

# sorting a array
# import numpy as np
# arr = [7, 2, 9, 1, 5]
# n=len(arr)
# print(arr)
# for i in range(len(arr)):
#     for j in range(n-i-1):
#         if arr[j]> arr[j+1]:
#             y = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = y 
    
# print(arr)

# print(arr[-1])
# print(arr[0])
# print(arr[-2])
#ok done