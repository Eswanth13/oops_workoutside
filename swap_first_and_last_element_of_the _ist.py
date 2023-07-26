# def myfun(list):
#     list[0],list[-1]=list[-1],list[0]
#     print(list)
# myfun([1,2,3,4,56])


def myfun(list):
    get = list[0], list[2]
    list[2], list[0] = get
    print(list)
myfun([1,2,3,4,56])


