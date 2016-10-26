#!/usr/bin/env python

print("Copy list")

a = ['spam', 'ham', 'egg']
b = a
c = a[:]
d = [v for v in a]

print("orig a: ", a)
print("copy b: ", b)
print("slice c: ", c)
print("loop d: ", b)
print("a is b: ", a is b)
print("a is c: ", a is c)
print("a is d: ", a is d)

print("Change a")

a[0] = "hoge"

print("orig a: ", a)
print("copy b: ", b)
print("slice c: ", c)
print("loop d: ", d)
print("a is b: ", a is b)
print("a is c: ", a is c)
print("a is d: ", a is d)
