# Написать функцию-декоратор для кеширования значений функции  seq(n) (1 + n) ** n возвращает [x1, x2, x3, , , , xn](n = 0 ....N)
# (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)
from functools import wraps
import datetime
import time


def timer(func):
    def wrapper(args):
        start = time.time_ns()
        res = func(args)
        finish = time.time_ns()
        print(f"Время выполнения: {finish - start}")
        return res

    return wrapper


def cacher(func):
    cach = {}

    def wrapper(args):
        key = args
        if key not in cach:
            cach[key] = func(args)
        print(cach)
        return cach[key]

    return wrapper


def logger(func):

    def wrapper(args):
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'функция: {func.__name__}\t'
        log_msg += f"аргумент: {args}\t"
        res = func(args)
        log_msg += f'результат: {res}\n'
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res

    return wrapper


@timer
@cacher
@logger
def seq(n):
    my_seq = []
    for i in range(0, n):
        my_seq.append((1 + i) ** i)
    return my_seq


seq(5)
seq(4)
seq(9)
