# list1=[1,12,3,4,5,6,7,8,9]
# list_sum=0
#
# for num in list1:
#      list_sum=list_sum+num
#      print(list_sum)

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
#     print(f'{a} is alindrome')
# else:
#     print(f"{a} is not a palindrom")

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

# string='i am a good boyasdd'
# count=0
# for i in string:
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
def myfun(*args):
    return list(set(args))
result = myfun(1, 2, 3, 2, 4, 1, 5,7,8,9,0)
print(tuple(result))














