transactions = [120, 350, 50, 400, 90, 220]
transactions_euro = [ i * 0.92 for i in transactions if i > 200 ]
print(transactions)
print(transactions_euro)

words = ["apple", "banana", "cherry", "kiwi"]

len_words = {x: len(x) for x in words}

print(len_words)


celsius = [0, 10, 20, 30, 40, 50]

faringate = {far: far * 9/5 + 32 for far in celsius}
print(faringate)


result = lambda x: x[::-1]

print(result("привет"))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sq = list(map(lambda x: x ** 2, numbers))
print(sq)

chet = list(filter(lambda x: x % 2 == 0, numbers))
print(chet)

from functools import reduce


sum = reduce(lambda x, y: x + y, numbers)
print(sum)


def select(input_function):
    def output_function():
        print("********************")
        input_function()
        print("********************")
    return output_function


@select
def hello():
    print("hello")

hello()

