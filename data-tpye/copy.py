a = 3
b = a
b = b + 1
print(b) # 4
print(a) # 3

## mutable 한 list, set, dictionary 의 경우 다음과 같이 함께 변하게 된다
c = [1, 2, 3, 4]
d = c

d[3] = 1
print(d) # [1, 2, 3, 1]
print(c) # [1, 2, 3, 1]

## 자료형의 복사 방법
d = c.copy()
d[3] = 4
print(d) # [1, 2, 3, 4]
print(c) # [1, 2, 3, 1]

## 다중 리스트에서는 주의해야 한다 .copy 는 딱 1차원 배열만 가능하다.
x = [1, 2, 3, [4, 5, 6]]
y = x.copy()

y[2] = 10
print(y) # [1, 2, 10, [4, 5, 6]]
print(x) # [1, 2, 3, [4, 5, 6]]

y[3][1] = 20
print(y) # [1, 2, 10, [4, 20, 6]]
print(x) # [1, 2, 3, [4, 20, 6]]

## 이걸 위해서는 deepcopy 를 해야한다.
import copy
y = copy.deepcopy(x)
y[3][2] = 40

print(y) # [1, 2, 3, [4, 20, 40]]
print(x) # [1, 2, 3, [4, 20, 6]]
