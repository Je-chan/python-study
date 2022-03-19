# 문자형
###  ₩ 가 escape 문자다.
### 실제로 ₩ 를 사용하고 싶다면 ₩₩ 로 두 번 입력하면 된다. 자바스크립트의 \ 과 같다고 보면 될듯.

## 1. 문자열과 숫자를 곱하면 문자열을 반복한다.
print('hello' * 3)


## 2. [] 를 사용해서 인덱스 값에 맞춰서 찾을 수 있다. 음수도 가능
a = 'Life is short, you need python'
print(a[1]) 
print(a[-6])


## 3. 슬라이싱 하는 방법은 : 를 사용한다
print(a[5:]) # is short, you need python
print(a[:5]) # Life
print(a[1:5]) # ife
print(a[2:-2]) # fe is short, you need pyth


## 4. 기본적으로 문자열은 데이터를 변경할 수 없어 슬라이싱을 많이 사용한다.
### a[0] = 'R' <= 이렇게 한 글자만 바꿀 수 없다는 것


## 5. 문자열과 관련된 함수
### 5-1. len : String 의 길이 값을 반환한다.
print(len(a)) # 30

### 5-2. startswith : 시작하는 부분을 검증
print(a.startswith('Life')) # True
print(a.startswith('Li')) # True
print(a.startswith('life')) # False

### 5-3. endswith : 끝나는 부분을 검증
print(a.endswith('python')) # True
print(a.endswith('javascript')) # False

### 5-4. find : 문자열 안에 해당 문자가 존재하는지 검증 후 시작하는 index 값을 반환
print(a.find('python')) # 24
print(a.find('javascript')) # -1

### 5-5. count : 특정 문자가 몇 번 나오는지를 알고 싶을 때
print(a.count('p')) # 1
print(a.count('a')) # 0

### 5-6. strip : 양 옆의 공백을 지우는 것
print('     --  --  --         '.strip()) 

### 5-7. 그외 replace, split, upper, lower, join => 자바스크립트와 유사함
#### join 의 경우, 인자로 받은 것들 인덱스 사이에 끼워 넣는다는 느낌으로 가지고 가면 된다.
print(','.join('abcd')) # a,b,c,d
print('/'.join(['a', 'b', 'c', 'd'])) # a/b/c/d



## 6. 포매팅
### 6-1. 첫 번째 방법 : {}.format()
print('지금은 {}시입니다'.format(7))
print('지금은 {}시 {}분입니다'.format(7, 49))
print('지금은 {time}시 {minute}분입니다.'.format(time=8, minute=50))

### 6-2. 두 번째 방법 : %
#### %d : 정수 / %s : 문자열 / %f : 실수 / %o : 8진수 / %x : 16진수
print('지금은 %d시 %d분입니다' % (7, 29))

#### 
num1 = 12
num2 = 3.567
s1 = '성공'
## 0.2 를 사용하면 소수점 둘 째자리 까지만 사용하겠다는 것을 의미
print("%d + %0.2f = %0.2f %s" % (num1, num2, num1 + num2, s1))  # 12 + 3.57 = 15.57 성공


## 7. 형 변환
x = 3
y = '30'
z = '30년'
f = '123.123'

print(str(x))
print(int(y))
# print(int(z)) 에러난다. => 자바스크립트라면 NaN 이 나올텐데 여기는 안 됨
print(float(f))
# print(float(z)) 에러난다. => 정수와 실수는 조금 엄격하게 구분된다.