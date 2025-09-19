# class SimpleIteration:
#     def __init__(self, number):
#         self.number = number
#         self.count = 0
#
#     def __next__(self):
#         if self.count < self.number:
#             self.count += 1
#             return 1
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self
#
# g = SimpleIteration(3)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#

# orders = ["Заказ #1001", "Заказ #1002", "Заказ #1003"]
# b = iter(orders)
# i = 0
# while True:
#     try:
#         print(next(b))
#     except StopIteration:
#         break
#


# gen =  (i for i in range(10))
# print(gen)
#
#
# def fun(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i
#
# for num in fun(10):
#     print(num)

# numb = [i+i for i in range(5)]
# print(numb)

#

# class Singleton:
#     __instances = None
#
#     @staticmethod
#     def getInstance():


import random
from random import randint

# new_list = {i: i + 2 for i in range(20)}
# print(new_list)