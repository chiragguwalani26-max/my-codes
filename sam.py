# a = 74108520963
# print(a)
# b= 'harry'
# print('type of b is',type(b))

# print((15%6))
# print((15/6))
# print((15//6))
# print((15**3))

# a = input("enter a no. = ")
# b = input("enter a no. = ")
# c = input(" + - * / ???")
# if(c == '+'):
#     print(int(a)+int(b))
# elif(c == '/'):
#     print(int(a)/int(b))
# elif(c == '-'):
#     print(int(a)-int(b))
# elif(c == '*'):
#     print(int(a)*int(b))
# else:
#     print ('try again')

# a = 5
# b = 3
# print('sol of 5 + 3 = ' , a + b)
# print('sol of 5 - 3 = ' , a - b)
# print('sol of 5 / 3 = ' , a / b)
# print('sol of 5 * 3 = ' , a * b) 

# # c = 1
# d = 8

# print (c + d)

# a = input('enter your name: ')
# print ('my name is : ' , a)

# a = "mango"
# b = len(a)
# print(a[-3:-1])
# print(a[3:5])

# print(a.upper())
# print(a.lower())
# print(a.replace("mango", "apple"))
# print(a.capitalize())
# print(a.center(50))
# print(a.count("mango"))
# print(a.endswith("l"))
# print(a.endswith("go"))
# print(a.find("g"))
# print(a.find("t"))
# # print(a.index("t"))
# print(a.islower())
# print(a.isspace())
# print(a.istitle())
# print(a.startswith("m"))

# x = 5
# y = 10

# temp = x 
# x=y
# y=temp

# x,y =y,x
# print(x ,y)

# def fac(num):
#     factorial = 1
#     if num < 0:
#         print('no. is negative')
#     elif num == 0:
#         print('no. is 0')
#     else:
#         for i in range(1 , num+1):
#             factorial = factorial*i
#         print("factorial of ", num,"is", factorial)
# fac(int(input('enter a no. - ')))

# import random
# num = random.randint(1,10)
# print(num)

# import random
# num = random.sample(range(1,100), 3)
# print(num)

# def fib(num):
#     a,b = 0,1
#     if num < 1:
#         print('null')
#     elif num == 1:
#         print(a)
#     elif num == 2:
#         print(a)
#         print(b)
#     elif num > 2 :
#         for _ in range(num - 2):
#             c = a + b
#             a,b=b,c
#             print (c)

# fib(int(input("enter a no.- ")))

# person = {
#     "name" : "Chirag",
#     "age" : 23,
#     "city" : "new york"
# }
# print (person)

# person["occupation"] = "business"
# print(person)

# del person["city"]
# print(person)

# def additon(num1, num2):
#     reslut = num1 +num2
#     return reslut
# sum = additon(3,5)
# print(sum)


# def say_hello():
#     print('Hellow World')
# say_hello()

# def calculate_area(lenght, width):
#     result=lenght * width
#     return result
# l = int(input('enter lenght:-' ))
# w = int(input('enter width:- '))

# print(calculate_area(l,w))

# def cal_Si(p,r,t):
#     SI = (p*r*t)/100
#     return SI
# p = int(input("principal:- "))
# r = float(input("rate:- "))
# t = float(input("time(years):- "))

# print(cal_Si(p,r,t))

# a = float(input("hello whats the time:- "))

#if - else

# if(20 <= a <= 24):
#     print('good night')
# elif(17 <= a <=19.59):
#     print('good eveing')
# elif(12 <= a <=16.59):
#     print('good afternoon')
# elif(5 <= a <=11.59):
#     print('good moring')
# else:
#     print('pls enter valid time')

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)

# if (20:00:00 <= timestamp <= 23:59:59)
#     print("good night")

# import time
# timestamp = time.strftime('%H,%M,%S')
# hour = int(time.strftime('%H'))
# hour = int(input('enter hours : -'))
# print(hour)

# if(hour > 0 and hour < 12 ):
#     print('good mrg')


# a = int(input('enter the amount:- '))
# if(a < 1000):
#     b = (a*5)/100
#     print(b) 
# elif(1001 <= a <= 5000):
#     b = (a*10)/100
#     print(b)
# elif(a >= 5001):
#     b = (a*15)/100
#     print(b)
# else:
#     print('you are not aligible for discount')
# print("purachse value after discount " , int(a) - int(b))

# a = int(input('enter the hrs :- '))
# if(a <= 2):
#     print("pay 100")
# elif(2 < a <= 5):
#     print("pay 50")
# elif(a > 5):
#     print("pay 20")
# else:
#     print('no fee')

# amount = int(input('Enter the amount :- '))

# if amount < 1000:
#     c = (amount * 5)/100
# elif amount < 5000:
#     c = (amount * 10)/100
# else:
#     c = (amount * 15)/100
# print(amount - c) 

# b = int(input("enter the battery : - "))
# m_input = input("metting time : - ").split()

# count = 0

# for i in m_input:
#     time = int(i)
    
#     if int(time) >= b:
#         count += 1
# print(count)
    
# for k in range(1, 20 , 3):
#     print(k)

# i = int(input("ente the no:- "))
# while(i<=3):
#     print(i)
#     i = int(input("ente the no:- "))

# print("done with the loop")
# count = 5
# while(count > 0):
#     print(count)
#     count -= 1

# for i in range(11):
#     if (i==10):
#         print("skip the iteration")
#         continue
#     print(5*(i + 1))


# functions

# def cal(a,b):
#     mean = ((a*b)/(a+b))
#     print(mean)
# def isGreater(a,b):
#     if(a>b):
#         print('a is greater')
#     elif(a==b):
#         print('both are sam')
#     else:
#         print('b is greater')
# def isLessser(a,b):
#     pass     
# a= 8
# b=4
# # mean = ((a*b)/(a+b))
# # print(mean)
# cal(a,b)
# isGreater(a,b)

# c= 10
# d= 20
# # mean = ((c*d)/(c+d))
# # print(mean)
# cal(c,d)
# isGreater(c,d)

#arguments

# def name(fname ='sam', mname ='sunil', lname = 'guwalani'):
#     print(fname,mname,lname)
# name('chirag', 'khan', 'jain')


# marks= [3, 5,6,"harry",True]

# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[-3])
# print(marks[len(marks)-3]) 

# print(marks)
# print(marks[2:])
# print(marks[1:len(marks)-1])

# tuple


# tup = [1,5,8,"sam", True]

# print(len(tup))
# print(tup[2])
# if 3421 in tup:
#     print("yess")

# tup2 = tup[1:4]
# print(tup2)

# tuple = (1,2,3,7,4,2,5,8,9,6,3,5,2,2)
# res = tuple.count(3)
# res = tuple.index(5)
# res = tuple.index(8,4,9)
# res =len(tuple)
# print(res)

# edge = (1,2,3,7,4,2,5,8,9,6,3,5,2)
# temp =list(edge)
# temp.append(56)
# temp.pop(8)
# edge = tuple(temp)
# print(edge)

# import time
# timestamp = time.strftime('%H,%M,%S')
# hour = int(time.strftime('%H'))
# hour = int(input('enter hours : -'))
# print(hour)

# if(hour > 0 and hour < 12 ):
#     print('good mrg')

#create program like kbc(kaun bange coreepati

# stock_price = [296,289,320,301,292]
# print(stock_price[0],stock_price[2])
#array

# expence = [2200, 2350, 2600, 2130, 2190]

# print('In Feb, how many dollars you spent extra compare to January = ', expence[1] - expence[0] )
# print('2. Find out your total expense in first quarter (first three months) of the year.')
# print(expence[0] + expence[1] + expence[2])
# print('3. Find out if you spent exactly 2000 dollars in any month')
# if 2000 in expence:
#     print('yes')
# else:
#     print('no')
# print('June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list')
# expence.append(1980)
# print('5. You returned an item that you bought in a month of April and got a refund of 200$.') 
# expence[3] -= 200
# print(expence)

# heros=['spider man','thor','hulk','iron man','captain america']

# # 1. Length of the list
# print(len(heros))
# # 2. Add 'black panther' at the end of this list
# heros.append('black panther')
# # 3. You realize that you need to add 'black panther' after 'hulk',
# heros.remove('black panther')
# #    so remove it from the list first and then add it after 'hulk'
# heros.insert(3, 'black panther')
# # 4. Now you don't like thor and hulk because they get angry easily :)
# #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# #    Do that with one line of code.
# heros[1:3]=['dr. strange']
# # 5. Sort the heros list in alphabetical order 

# # (Hint. Use dir() functions to list down all functions available in list)
# heros.sort()
# print(heros)


# l = 'hey my name is {} and im form {} ' 
# country = 'india'
# name = 'sam'
# print(f'hey my name is {name} and im form {country}')
# print(l.format(country,name))

#doc string
# def square(n):
#     '''take in a number n and returns square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__)

# recursion
# def factorial(f):
#     if(f==0 or f==1):
#         return 1
#     else:
#         return f * factorial(f - 1)
# print(factorial(5),factorial(4),factorial(3))

# def fibonachi(n):
#     if(n==0 ):
#         return 0
#     elif( n==1):  
#         return 1
#     else:
#         return fibonachi(n - 1) + fibonachi(n - 2)
# print(fibonachi(6))
# print(fibonachi(7))
# print(fibonachi(30))

#set
# set = {1,2,85,96,45,21,1,2}
# print(set)
# set = set()
# print(type(set))
# for vlaue in set:
#     print(vlaue)


# set = {1,2,85,96,45,21,1,2}
# set2 ={45, 26, 66 ,88, 77, 66}
# # print(set.union(set2))
# # set.update(set2)
# # print(set)
# set3 = set.difference(set2)
# print(set3)

#dictonatory

# dec = {
#     'name':'sam' , 'age': 22 , "elgible": True
#     }
# print(dec)
# print(dec['name'])
# print(dec.get('name'))

# print(dec.keys())
# print(dec.values())

# for key in dec.keys():
#     print(dec[key])
#     print(f"the value {key} is correspondin to {dec[key]}")
# print(dec.items())
# for key, value in dec.items():
#     print(f'his {key} is {value}')


# for i in range(5):
#     print(i)
#     if i==4:
#         break
# else:
#     print('end pf loop')

# i= 0
# while i<6:
#     print(i)
#     i += 1
#     if i==6:
#         break
# else:
#     print('sorry')

#xceptional handlind(erreo handling)

# a = input('enter the number')
# print(f"multiplaction tbale of {a} is ")
# try:
#     for i in range(1,11):
#         print(f'{int(a)} X {i} = {int(a)*i}')
# except:
#     print('invalid input')

# print('some thing need to be private')
# print ('good to go ') 

#finally:
# try:
#     l= [1,2,3,4,5]
#     i =int(input('enter th index'))
#     print(l[i])
# except:
#     print('some error')
    
# finally:    
#     print(' have a good day')
# print('have a parle-G')

#finally with function(def)
# def cal():
#     try:
#         l= [1,2,3,4,5]
#         i =int(input('enter th index'))
#         print(l[i])
#         return 1
#     except:
#         print('some error')
#         return 0
#     finally:    
#         print(' have a good day')
#     print('have a parle-G')
# x= cal()
# print(x)

# def x():
#     a = input("enter the no. btw 5 and 9 ")

#     if a == 'quit':
#         print('goood byeee')
#         return 
#     else:
#         if(int(a)<5 or int(a)>9):
#             raise ValueError('value is not in btw 5 and 9 ')
#         else:
#             return a
    
# y = x()
# print(y)
 
# #kbc
# print('welcome to kbc')
# print('type 1-A 2-B 3-C 4-D')
# questions = [
# ['What_is_the_capital_of_India_?', 'A : Mumbai', 'B : New_Delhi', 'C : Kolkata', 'D : Chennai', 2],

# ['In_computers_what_does_CPU_stand_for_?', 'A : Central_Process_Unit', 'B : Central_Processing_Unit', 'C : Computer_Processing_Unit', 'D : Control_Processing_Unit', 2],

# ['Which_planet_is_called_the_Red_Planet_?', 'A : Venus', 'B : Jupiter', 'C : Mars', 'D : Saturn', 3],

# ['Who_is_known_as_the_Father_of_the_Indian_Constitution_?', 'A : Mahatma_Gandhi', 'B : Jawaharlal_Nehru', 'C : Dr_B_R_Ambedkar', 'D : Sardar_Patel', 3],

# ['Which_programming_language_is_known_for_Data_Analysis_and_AI_?', 'A : HTML', 'B : CSS', 'C : Python', 'D : SQL', 3]

# ]  


# amount = [1000, 5000, 100000, 150000, 200000]


# for i in range(len(questions)):
#     print(questions[i][0])
#     print(questions[i][1])
#     print(questions[i][2])
#     print(questions[i][3])
#     print(questions[i][4])
    
#     ans = int(input())
#     if ans  == questions[i][5] :
#         print(f'you won {amount[i]}')
#     else:
#         print('wrong answer')
#         if(i == 0):
#             print('you worn 0') 
#         else:
#             print('you won ' , amount[i-1])
#         break


# a=330
# b=3303
# print("A") if (a>b) else print("=") if(a==b) else print("B")

# arr = [32,80,53,96,72,86,72,90]
# index = 0
# for i in arr :
#     print(i, end =" ")
#     print("well done sam!",end =" ") if (index == 3) else None
#     index +=1 

# import math
# x=math.sqrt(9)
# print(x)

# from math import sqrt
# x= sqrt(9)
# print(x)

# from math import *
# x = sqrt(9) * pi
# print

# import math
# print(dir(math))

# from dsa import fib
# print(fib(3))
# print(fib(12))   
# print(fib(10))


# def welcome():
#     print('hello chirag')
    
#     print(__name__)

# if __name__ =="__main__":
#     welcome()

# local nad global varible
# x=10
# def fun():
#     global x
#     x=4
#     y=5
#     print(y)
# fun()
# print(x)
# # print(y) 

#sanke water gun

# import random
# print("0= sanke , 1 = water , 2 = gun")
# x = int(input("enter the your value:- "))
# y = random.randint(0,2)
# def sankeGame(player, computer):
#     if (computer == player):
#         return 0
#     if (computer == 1 and  player == 2):
#         return -1
    
#     if (computer ==2 and player == 0):
#         return -1
    
#     if (computer == 0 and player == 1):
#         return -1
#     return 1
# score = sankeGame(x, y)
# print("you", x)
# print("computer", y)

# if (score==0):
#     print('its draw')
# elif (score==1):
#     print('you win')
# else:
#     print('computer win')


# class person:
#     name = 'sam'
#     occ = 'swe'
#     net_worth ='10'
    

# a = person()
# a.name = 'chirag'
# a.occ = 'accoutant'
# print(a.name, a.occ)


# class person:
#     name = 'harshit'
#     occ = 'SWE'
#     net_worth ='10'
    
#     def info(self):
#        print(f'{self.name} is a {self.occ}')

# #self= woh objct jis pe ye mothod call ho rah aha

# a = person()
# a.name = 'chirag'
# a.occ = 'accoutant'
# a.info()


# b = person()
# b.occ = 'actor'
# b.name = 'sam'
# b.info()


# c = person()
# c.name = 'yash'
# c.occ = 'software engineer'
# c.info()

# d = person()
# d.info()

# construtor(__init__)
class person:
    
    def __init__(self,n,o):
        print('hey im a person')
        self.name = n
        self.occ= o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person('DIYA','CA')
b=person('CHIRAG','ER')
c=person('SAM','SWD')
a.info()
b.info()
c.info()

