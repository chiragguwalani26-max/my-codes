# import shutil

# for i in range(1, 101):
#     shutil.rmtree(f"so module/Perfect Shot {i}")

#reading a file
# f= open('myfile.txt','rb')
# # print(f)
# text= f.read()
# print(text)
# f.close 

# f = open('myfile.txt','a')
# f.write(" hello chirag",)
# f.close()

# with open('myfile.txt','a')as f:
#     f.write(' hii im inside it ')

# f =open("myfile.txt", 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break
    
#read.line()
# f =open("myfile.txt", 'r')
# i= 0
# while True:
#     i=i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"marks of student{i} is : {m1*2}")
#     print(f"marks of student{i} is : {m2*2}")
#     print(f"marks of student{i} is : {m3*2}")

#writeline()

#lamba function

# def fun(x):
#     return x*2
# print(fun(2))


# double = lambda x:x*2
# cube = lambda x:x*x*x

# print(double(2))
# print(cube(2))

# function inside lambda function
# def app(fc,value):
#     return 10 + fc(value)
# print(app(lambda x:x*x*x,2))

#map filter and reduce

# def fun(x):
#     return x*x*x
# print(fun(2))

# n=[1,5,8,9,6,4,2,3]
# new=[]
# for i in n:
#     new.append(fun(i))
#     #map function
# newl = list(map(fun,n))

# print(new)
# print(newl)

# #filter
# def run(value):
#     return value >2
    
# newfil = list(filter(run, n))
# print(newfil)

# newfil = list(filter(lambda x:x>2,n))
# print(newfil)


# #reduce
# from functools import reduce

# def re(a,b):
#     return a+b
# newred = reduce(re,n)
# print(newred)
# newred = reduce(lambda a,b:a+b,n)
# print(newred)