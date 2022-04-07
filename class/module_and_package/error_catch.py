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

a = 6
assert a >= 10, "값이 작습니다"
