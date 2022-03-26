# 1. 파라미터 기본값 설정
## 파라미터에 기본값을 설정해줄 수 있다.
def addition(a=1, b=3):
  return a+b

print(addition())
print(addition(6))
print(addition(b=0))

# 아래의 코드는 불가능하다. 만약 파라미터에 값을 대입하는 방식을 적용하고 싶다면 대입하는 파라미터는 마지막에 적어야 한다.
# print(addition(a=2, 5))

# 이 아래의 코드도 불가능하다. a는 첫 번째 파라미터인데 첫 번째 파라미터에 값이 들어갔기 때문
# print((addition(5, a=2)))

print(addition(2, b=5))

# 2. args
## 파라미터는 *args 를 사용해서 파라미터로 받은 모든 값들을 튜플의 형태로 가져올 수 있다
## 함수를 정의할 때, *args 를 넣는다
## args 대신에 다른 이름을 넣어도 되지만 편의상 args 를 사용한다

def printer(*args):
  for i in args:
    print(i)

printer(10, 20, 30, 40)

# 3. kargs
## args 가 튜플이라면 kargs로 들어간 인수들은 딕셔너리의 형태로 변환된다.
## 즉, kargs 를 사용하기 위해서는 변수명을 적어서 파라미터를 작성해야 한다.
## kargs 를 사용할 때는 ** 로 애스터리스크가 두 개 들어간다.

def kargsPrinter(**kargs):
  return kargs

print(kargsPrinter(a=1, b=2, c=3))


# 4. global 명령어
## global 명령어는 함수 밖에 있는 변수 값을 가지고 오겠따는 것을 의미한다.

num = 10

def localNum ():
  num = 20
  print('local', num)
  
def globalNum():
  global num
  num += 20
  print('global', num)
  
print('original', num)
localNum()
globalNum()
print('after', num)

# 5. 파이썬 함수 작성 규칙
## 변수 이름과 함수 이름은 소문자로, 여러 단어일 경우 _ 로 나눈다
## 적당한 띄어쓰기로 가독성을 높인다
## 적당한 변수명 및 함수명 선언으로 남이 봐도 이해할 수 있도록 한다.