# -*- coding: utf-8 -*-

def fib():
    a,b = 0,1
    while a <= 55:
        yield a
        a,b = b, a+b

items = []

# appendごとにprintがうまくかけない
[items.append(v) for v in fib()]
print items

