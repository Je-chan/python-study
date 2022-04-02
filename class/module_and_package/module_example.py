# 1. 모듈
import my_module

print(my_module.variable)
print(my_module.addition(10, 20))

# import 를 하는 방법으로
# > import 모듈
# > from 모듈 import 함수이름1, 함수이름2
# >> 이렇게 사용할 경우, my_module.함수이름1 이런식으로 쓰지 않고, 바로 함수이름1 로 사용할 수 있다.
# > from 모듈 import 모듈 *
# >> 이렇게 사용하면 my_module 안에 존재하는 모든 것을 가져와서 사용할 수 있다. ㄴ
from my_module import *
print(variable)

# > 만약 이름을 바꾸고 싶다면, as 바꿀이름 으로 사용하면 된다.

# 만약 모듈을 갖고 오고 싶으 폴더를 확인하고 싶다면? sys.path 로 확인
# > 가져올 경로를 추가하고 싶다면 sys.path.append('검색경로') 로 가져온다.
# > sys.path 의 순서도 중요하다. 서로 다릉 모듈에 같은 함수명이 있을 때, 가져오는 함수는 sys.path의 순서대로 가져온다

# __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수다.
# > 현재 실행중인 파일의 이름은 __main__
print(__name__)
# > 불러온 모듈의 경우, 모듈의 이름은 __name__ 이란 변수에 저장된다
# >> 현재 이거는 import my_module 했을 떄, print 됐다.


# 2. 패키지
# 패키지는 모듈의 모임이라고 생각하면 된다. 파이썬 3.3 버전 이전에는 __init__.py 가 있어야만 패키지로 인정된다.
# from 패키지 import 모듈명
# import 패키지.모듈명
from test_package import test_module1
import test_package.test_module2

# 패키지 안에 모든 모듈을 불러오려면?
# > __init__.py 파일 안에 __all__ 에 리스트로 모듈 이름을 직접 모두 적어주면, 적은 모듈이 * 로 호출된다.
# > 모듈 이름을 적을 때 작은 따옴표를 사용해야 한다.
from test_package import *
