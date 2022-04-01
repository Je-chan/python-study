# lambda 함수
# > 이름이 없는 한 줄 짜리 함수. 보통 함수의 매개 변수로 들어 간다
# > 람다 함수는 그 자체로 쓰이기 보다는 다른 함수와 연계해서 굉장히 중요하게 사용된다.
def run(func, x):
    print(func(x))


run(lambda x: x + 1, 2)
