def myfun(year):
    if (year%400==0)and (year%100==0)or (year%4==0)and(year%100==0):
        return f'{year} is leepyear'

    else:
        return f'{year} is not a leepyear'
a=int(input('enter a number : '))
print(myfun(a))
