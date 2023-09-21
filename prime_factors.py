def prime_factors(num):
    factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors

num = int(input("Enter a number: "))
if num < 1:
    print("Please enter a positive integer.")
else:
    factors = prime_factors(num)
    print(f"The prime factors of {num} are:", factors)

# def myfun(x):
#     prime_factor=[]
#     div = 2
#     while div <= x:
#         if x%div == 0:
#             prime_factor.append(div)
#             x=x//div
#         else:
#             div +=1
#     return prime_factor
# x = int(input("Enter a number: "))
# print(myfun(x))
