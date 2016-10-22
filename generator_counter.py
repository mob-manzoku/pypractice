#!/usr/bin/env python


def main():

    gnum = gen_num(begin=10, step=10)
    while True:
        input()
        print(next(gnum))


def gen_num(begin=0, step=1):
    n = begin
    while True:
        yield n
        n += step


if __name__ == "__main__":
    main()
