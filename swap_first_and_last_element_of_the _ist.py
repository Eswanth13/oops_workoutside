# def myfun(list):
#     if len(list)<2:
#         print("enter at least wo numbers")
#         return
#
#     list[0],list[-1]=list[-1],list[0]
#     print(list)
# myfun([1,2,3,4,5 ])


def myfun(input_list):
    if len(input_list) < 2:
        print("Please enter at least two numbers.")
        return

    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    print(input_list)

input_str = input("Enter the numbers separated by spaces: ")
input_list = [int(num) for num in input_str.split()]
myfun(input_list)




