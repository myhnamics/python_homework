import random
# 9.2
# def get_odd():
#     for i in range(10):
#         if i % 2 == 1:
#             yield i
#
# A = get_odd()
# print(type(A))
# print(get_odd())
#
# count = 1
# for i in get_odd():
#
#     if count == 3:
#         print(i)
#     count +=1

# 9.3
def start_end(func):
    def new_function():
        print('start')
        result = func()
        print('end')
        return result

    return new_function

def nothing():
    print('nothing')


start_nothing = start_end(nothing)

start_nothing()





# 9.4
