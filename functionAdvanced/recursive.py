# 재귀 함수
## 반드시 종료 조건을 분명하게 작성해야 한다. 그렇지 못한 경우 메모리를 투가적으로 많이 사용해서 스택오버플로우가 발생한다.
def func(count):
    if count > 0:
        print(count, '현재')
        func(count-1)
    print('결과', count)

func(10)

