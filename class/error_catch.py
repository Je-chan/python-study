# try:
#   (에러문장)
# except Exception as e:  => as e 라고 적으면 발생할 에러문이 string 의 형태로 e에 저장된다.
#   print(e) => 에러났을  때 실행할 문장
# else :  => 에러가 안 나면 실행할 문장
# finally : => 에러 발생 여부와 상관없이 실행될 문장

try:
    1 / 0
except Exception as e:
    print(e)
    print('에러!')

# raise Exception("강제로 에러를 발생시킴")
# >  rasise 문을 사용해서 우측의 스트링에 에러를 만든다.

# raise Exception('내가 만드는 에러')

# assert (조건), (String)
# assert 로 시작하는 문장에 조건식을 적으면,  조건을 만족하지 않을 경우, error가 발생하며 우측의 String 을 출력한다

# a = 6
# assert a >= 10, "값이 작습니다"

a = 0
while a < 5:
    try:
        li = [1, 2, 3]
        print('인덱스 번호를 입력')
        num1 = input()
        if num1 == 'x': break
        num = int(num1)
        print('{} / 2 = {}'.format(li[num], li[num] / 2))
    except Exception as err:
        print('{} 라는 에러 발생'.format(err))
    else:
        print('제대로 된 입력')
    finally:
        print('에러가 나든 말든 출력되는 문구')
        a += 1

# 에러 객체를 사용해 해당 에러일 때 사용할 로직을 만들 수 있다
try:
    4 / 0
except TypeError:
    print('type Error 가 난 거를 출력')
except ZeroDivisionError:
    print('0으로 나눴지?')
except IndexError:
    print('인덱스 에러야..')


# 나만의 에러를 지정할 수도 있다
# Exception 이라는 에러조차 클래스기 때문
class MyException(Exception):
    def __init__(self, arg):
        super().__init__('정수가 아니다 : {}'.format(arg))


def conver(num):
    if num.isdigit():
        return int(num)
    else:
        raise MyException(num)


try:
    print('숫자를 입력')
    num = input()
    a = conver(num)

except MyException as err:
    print('에러: {}'.format(err))
else:
    print('입력한 수 {} 타입 {}'.format(a, type(a)))
