# 중첩 함수

def func1(a):
    def func2():
        # 이 nonlocal 이 func1 의 파라미터로 받는 a 를 가져오겠다는 의미
        nonlocal a
        a = a + 1
        return a

    return func2()


print(func1(2))

a = 10


def func3(a):
    def func4():
        # global은 완전히 바깥에 있는 걸 가져온다
        global a
        a = a + 1
        return a

    return func4()


print(func3(2))
