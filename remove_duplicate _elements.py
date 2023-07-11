#----Write a Python program to remove duplicate elements from a list.
string=[1,2,3,9,2,3,6,8,6,3,5,6,3,4,5,7,8,9,0,2,5,6,7,8]
str1=[]
for i in string:
    if i not in str1:
        str1.append(i)
print(list(set(str1)))

#Another method
string=[1,2,3,9,2,3,6,8,6,3,5,6,3,4,5,7,8,9,0,2,5,123,6,7,8]
remove_duplicate_values=set(string)
print(remove_duplicate_values)


#Another method
def myfun(*args):
    return list(set(args))
result = myfun(1, 2, 9,3, 2, 4, 1, 5,7,8,9,0)
print(tuple(result))
