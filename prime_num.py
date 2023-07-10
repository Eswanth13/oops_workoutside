num=int(input('enter the number: '))
check=False
if num==1:
    print(f'{num} is not a prime')
elif num>1:
    for i in range(2,num):
        if num%i==0:
            check=True
            break
    if check==True:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is prime number")
