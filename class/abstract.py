from abc import *


# 추상 클래스는 자기 인스턴스를 만들 수 없다
# 추상 메소드라는 @abstract 데코레이터를 사용해 자기 하위객체에게 특정 메소드 생성을 강제할 수 있다.
# > 한 마디로, Abstract 를 상속 받은 클래스는 반드시 method 라는 메소드 생성을 강제한다는 것
class Abstract(metaclass=ABCMeta):
    @abstractmethod
    def method(self):
        pass


class test(Abstract):
    def method(self):
        pass


test1 = test()

# isinstance(변수, 클래스 이름)
# > 주어진 변수가 해당 클래스의 인스턴스인지 확인하는 것

a = 3

print(isinstance(a, int))
print(isinstance(test1, int))