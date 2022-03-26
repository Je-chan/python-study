# For 문
## for 문을 돌릴 수 있는 데이터 형식은 list, tuple 등이 있다
## 순서열은 아니더라도 set 이나 dictionary 도 들어갈 수는 있다.
for i in [1, 2, 3, 4]:
  print(i)

for i in set([11,52,42, 144]):
  # set 은 순서가 없기 때문에 요소의 순서대로 출력되지 않는다.
  print(i)
  
## 1. range 함수
### range(num1, num2) 로 쓰면, num1에서부터 시작해 1씩 증가해 num2 직전까지 증가해서 만들어진 list다.
### range(num1) 로 쓰면 0 ~ num1 까지로 출력한다.
### range(num1, num2, 2) 로 쓰면, num1에서부터 시작해 2씩 증가한다
for i in range(1, 5):
  print(i)

for i in range(1, 100, 10):
  print(i)