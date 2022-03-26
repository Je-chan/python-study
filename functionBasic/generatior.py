# 1. yield
## yield 를 통해 생성된 값들은 바로 계산되는 것이 아니라 호출됐을 때 계산이 된다.
## lazy operation

from re import L
from tkinter import N


def gen(n):
  while n > 0:
    yield n
    n = n - 1
    
print(gen(10)) # <generator object gen at 0x7fe291e589e0>

a = gen(10)
print(a) # <generator object gen at 0x7fc890e889e0>

## yield 는 gen(10)은 yield 로 지금 바로 계산되지 않은 상태. 다른 명령어로 호출을 해야지만이 사용이 가능해진다

print(list(a)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in gen(10):
  print(i)