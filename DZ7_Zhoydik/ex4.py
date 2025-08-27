# Сделать декоратор, который измеряет время,
# затраченное на выполнение декорируемой функции.
import time

def timer(fun1):
    def timing (*args, **kwargs):
        start = time.time()
        result = fun1(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result, end-start
    return timing

@timer
def fast_fun():
    time.sleep(1)
    print(f"fast function")

@timer
def slow_fun():
    time.sleep(4)
    print(f"slow function")

fast_fun()
slow_fun()
