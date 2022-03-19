# 매핑형 자료 - Dictionary (파이썬에서는 딕셔너리로 매핑형 자료를 사용)
## key - value 의 형태로 주어진 데이터들의 집합
## key 에는 순서가 없고 중복도 없다
## key 자료형에는 일반적으로 문자열을 사용한다. 숫자형도 사용할 수 있고 타입이 자유로우나 mutable 한 것들은 모두 안 된다.( key 가 변하면 안 되기 떄문 )
## {key: value} 로 사용한다

a = {'name': '박예찬', 'tall': '184', 3: '무언가'}
print(a) 
print(a['name'])
print(a[3])

## 아예 처음부터 빈 딕셔너리를 만들어서 사용할 수 있다.
b = {} # 이렇게 할 수도 있고 => 참고로 이렇게 만들면 딕셔러니가 되지, set 이 되는 게 아님
b = dict() # 이렇게 할 수도 있음
b['name'] = 'je'
print(b)

## 1. 주요 함수들
### 1-1) len : 길이 반환
print(len(a)) # 3

### 1-2) del : 데이터 삭제
del a[3]
print(a) # {'name': '박예찬', 'tall': '184'}

### 1-3) keys() : key 값 모두 반환
print(a.keys()) # dict_keys(['name', 'tall'])

### 1-4) values() : value 값 모두 반환
print(a.values()) # dict_values(['박예찬', '184'])

### 1-5) get() : 해당 key 값의 value 를 가져오는 것. 만약 해당 key 가 없다면 None을 반환한다.
# print(a[123]) => 에러를 발생시킨다
print(a.get(123)) # None
