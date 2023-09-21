# list1=[1,12,3,4,5,6,7,8,9]
# #list1=[1,2,3]
# list_sum=0
#
# for num in list1:
#      list_sum=list_sum+num
# print(list_sum)

# num=11351345
# stri=str(num)
# a=[]
# for i in stri:
#      a.append(int(i))
# print(sum(a))

# def myfun(number):
#      a = []
#      for i in str(number):
#           a.append(int(i))
#      print(sum(a))
#
# myfun(int(input('enter the num:')))


#---------MAX OF TWO NUM--------
# a=(int(input('enter the num:')))
# b=(int(input('enter the num:')))
# if a>b:
#     print(f'a is max{a}')
# else:
#     print(f'{b} b is max')


#----finding maxnumbers by using function-----
# def maxnum(numbers):
#     return max(numbers)
# numbers=[1,2,3,4,9,6]
# result=maxnum(numbers)
# print(result)

#----finding maxnumbers by using *args------

# def myfun(*args):
#     return max(args)
# maxnumber=myfun(2,3,45,9,6)
# print(maxnumber)



#-------factorial-----
# number = int(input("Enter a number: "))
# factorial = 1
#
# for i in range(1, number + 1):
#         factorial *= i
# print(factorial)


#--------Fibonacci series.-----

# limit=int(input('enter the number: '))
# a=0
# b=1
# fibonacci_series=[]
# while limit>=b:
#     x=a+b
#     if x<=limit:
#         fibonacci_series.append(x)
#     a=b
#     b=x
# print(fibonacci_series)


#---------palindrome------

# string =str(input("enter the string: "))
# a=string[::-1]
# if a==string:
#     print(f'{a} is palindrome')
# else:
#     print("it is not a palindrom")

#Another method
# def myfun(b):
#     a = b[::-1]
#     if a==b:
#         print(f'{b} is palindrome')
#     else:
#         print(f"{b} is not a palindrom")
# print(myfun(input('enter the string:')))

#-------Write a Python program to count the occurrence of a character in a string.---

# string = input("enter a string: ")
# letter = input("enter a letter: ")
#
# occurrence_count = 0
# for char in string:
#     if char == letter:
#         occurrence_count += 1
#
# print(f"The character '{letter}' occurs {occurrence_count} times in the string.")
#


#------Write a Python program to find the length of a string---------

#string='i am a good boyasdd'
# count=0
#for i in enumerate(string):
#     if i==' ':
#         continue
#     else:
#         count =count +1
# print(count)


#Write a Python program to remove the leading and trailing whitespaces from a string.-----

# string=" hello world "
# print(string)
# a=string.strip()
# print(a)

#----Write a Python program to remove duplicate elements from a list.
# string=[1,2,3,9,2,3,6,8,6,3,5,6,3,4,5,7,8,9,0,2,5,6,7,8]
# str1=[]
# for i in string:
#     if i not in str1:
#         str1.append(i)
# print(str1)

#Another method
# string=[1,2,3,9,2,3,6,8,6,3,5,6,3,4,5,7,8,9,0,2,5,123,6,7,8]
# remove_duplicate_values=set(string)
# print(list(remove_duplicate_values))


#Another method
# def myfun(*args):
#     return list(set(args))
# result = myfun(1, 2, 3, 2, 4, 1, 5,7,8,9,0)
# print(tuple(result))

#Write a Python program to find the greatest common divisor (GCD) of two numbers.

# import math
# print(math.lcm(63, 48))
# print("The gcd of 60 and 48 is : ", end="")

# def myfun(a,b):
#     if b==0:
#         return a
#     else:
#         return myfun(b,a%b)
# a=int(input('enter the number a : '))
# b=int(input('enter the number b : '))
# print(myfun(a,b))

#------Write a Python program to check if a number is a perfect square.------

# import math
# number = int(input("Enter the Number: "))
#
# root = math.sqrt(number)
# if int(root) ** 2 == number:
#     print(number, "is a perfect square")
# else:
#     print(number, "is not a perfect square")


#-------Write a Python program to find the ASCII value of a character.
# a=str(str(input('enter the value: ')))
# print(ord(a))
# x=1
# print(x<<2)

# def askint():
#     while True:
#         try:
#             val = int(input("Please enter an integer: "))
#         except:
#             print("Looks like you did not enter an integer!")
#             continue
#         else:
#             print("Yep that's an integer!")
#             break
#         finally:
#             print("Finally, I executed!")
#         print(val)
# askint()
#


# -----leap year-----
# def myfun(year):
#     if (year%400==0)and (year%100==0)or (year%4==0)and(year%100==0):
#         return f'{year} is leepyear'
#
#     else:
#         return f'{year} is not a leepyear'
# a=int(input('enter a number : '))
# print(myfun(a))


#Write a Python program to remove all vowels from a string.

# def remove_vowels(input_string):
#     vowels = "AEIOUaeiou"
#     result = ''.join(char for char in input_string if char not in vowels)
#     return result
# input_string = input("Enter a string: ")
# output_string = remove_vowels(input_string)
# print("String without vowels:", output_string)


# ----another method----
# def remove_vowels(input_string):
#     vowels = "AEIOUaeiou"
#     results=''
#     for char in input_string:
#         if char not in vowels:
#             results += char
#     return results
# input_string = input("Enter a string: ")
# output_string = remove_vowels(input_string)
# print("String without vowels:", output_string)



#Write a Python program to find the number of uppercase and lowercase letters in a string.

# def count_upper_lower(text):
#     upper_count = 0
#     lower_count = 0
#
#     for char in text:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#
#     print(f'upper_count{upper_count}, lower_count{lower_count}')
#
#
# input_string = input("Enter a string: ")
# count_upper_lower(input_string)
#for i in range(len(check)-2,len(check)):
#     check[i].click()

# check=["*","$","@","%","^"]
# print(len(check))
# for i in range(len(check)-2,len(check)):
#      print(i)

# print("Question1: 2 +3 : ", 2 / 3)
# try:
#      print("Question2: 1/0 : ",1/0)
# except:
#      print("cannot divide by zero, changing divisor, Question2: 1/1 : ",1/1)
# print("Question3: 1/1 : ",1/1)


# def myfun(*a):
#     return sum(a)
# #c=myfun(2,3)
# print(myfun(2,3,4))

#
# x=lambda a:type(a)
# print(x(123))


# x=lambda *a: sum(a)
# print(x(2,3,4,4,5,78,9,0,))







# list1=[1,12,3,4,5,6,7,8,9]
# sum_list=0
#
# for i in list1:
#     sum_list=sum_list+i
# print(sum_list)


#list1=[1,12,3,4,5,6,7,8,9]

# def myfun(*args):
#     print(sum(args))
# myfun(1,12,3,4,5,6,7,8,9,)

# a=int(input("enter a number: "))
# b=str(a)
# sum_int=0
# for i in b:
#     sum_int=sum_int+int(i)
#print(sum_int)

#---------------------------
# for r in range(1,6):
#     for c in range(1,6-r+1):
#         print("*", end=" ")
#     print( )
#--------------------

# import math
# row = int(input("Enter the max rows : "))
# col = row * 2 - 1
# for r in range(1,row+1):
#     for c in range(1,col+1):
#         for index in range(1,r):
#
#     print()

#-------------------------------
# Items=["esw","asd","sdf","ghj","qwe"]
# elem=[]
# for elements in Items:
#     elm=elements
#     elem.append(elm)
#
# elem.sort(reverse=True)
# print(elem)

#-------------------------
#Write a Python program to generate the Fibonacci .series
# limit=int(input("enter a number: "))
# a=1
# b=1
# Fibonacci_series=[]
# while limit>=b:
#     x=a+b
#     if x<=limit:
#         Fibonacci_series.append(x)
#     a=b
#     b=x
# print(Fibonacci_series)

#--------------------------
a="1 2 3  4 5 6"
for i in a.split():
    print(type(int(i)))


