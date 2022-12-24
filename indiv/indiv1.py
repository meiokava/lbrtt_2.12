# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def external(start=0):
    def middle(func):
        def inner(*args):
            arg = args[0]
            return func(arg) + start
        return inner
    return middle


@external(start=5)
def sum_line(string):
    return sum(list(map(int, string.split())))


if __name__ == "__main__":
    numb = input("Please enter numbers with gaps: ")
    print(sum_line(numb))
