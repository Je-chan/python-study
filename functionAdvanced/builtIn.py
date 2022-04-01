# 유용한 내장 함수
# > abs(x) : 절댓값 반환
# > max([]) : 최댓값 반환 / min : 최솟값 반환
# > sorted([]) : 정렬
# > type(x) : x 의 자료형 반환
# > round (x, [,num]) :  x 를 소수 num 번째 자리 수까지 반올림 // default 값이 이미 존재해서 괄호를 쳤을뿐, 실제로 괄호를 치는 건 아니다
# > pow(x,y) : x의 y 제곱

print(type(3))
print(type('3'))
print(type([1, 2, 3, 4]))

print(round(3.141592))
print(round(3.141592, 0))
print(round(3.141592, 3))

# > enumerate : 반복문에 인덱스가 필요할 때, enumerate 명령을 사용해 리스트의 원소와 인덱스값을 모두 생성한다.

for index, i in enumerate(['하나', '둘', '셋', '넷']):
    print(index)
    print(i)

# > zip(리스트 1, 리스트 2) : 두 개의 리스트를 합쳐서 각 리스트의 원소 쌍을 원소로 갖는 리스트로 반환
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print(zip(list1, list2)) # 이것도 지금 generator
print(list(zip(list1, list2)))

# > map(함수, 컬렉션) : 컬렉션(list, tuple 등)의 모든 데이터를 함수의 매개변수로 대입해서 결과를 리턴
print(map(lambda x : x+1, [1, 2, 3, 4])) # 이것도 generator
print(list(map(lambda x: x+1, [1, 2, 3, 4])))

 # > filter(함수, 컬렉션) : 컬렉션의 모든 데이터를 함수의 매개변수로 대입홰 결과가 참인 멤버들을 반환
print(list(filter(lambda x: x%2 == 0, [1, 2, 3, 4]))) # 이것도 generator

