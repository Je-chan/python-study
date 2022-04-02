# 1. 정적 메소드 : 인스턴스를 생성하지 않고, 클래스를 이용해 직접 호출할 수 있는 메소드
# > 메소드 내의 멤버 변수를 호출할 수도 없고, self 매개변수도 사용하지 않는다
# > @staticmethod 데코레이터로 수식한다.
class human:
    def __init__(self, height, age):
        self.height = height
        self.age = age

    @staticmethod
    def think(think):
        return think + '를 생각하는 중입니다.'

    # 삭제 메소드
    def __del__(self):
        print('삭제 됐습니다!')


je = human(184, 28)
liebe = human(183, 25)

del liebe

# 따로 인스턴스를 생성하지 않아도 정적 메소드는 사용할 수 있다.
print(human.think('이게 정말 될까?'))


# 2.  클래스 메소드 : 정적 메소드와 유사하지만 첫 번재 변수로, 클래스 객체가 전달된다.
# > cls 매개 변수를 사용한다.
# > @classmebthod

class student:
    count = 0

    @classmethod
    def cmethod(cls):
        print('클래스 메소드')
        print(cls.count)

    @staticmethod
    def smethod():
        print('정적 메소드')


# 클래스 메소드는 자기 스스로 갖고 있는 변수에 접근이 가능하다.
# self 는 object 를 생성하는 거지만, cls 는 스스로를 받는다.
student.cmethod()
student.smethod()


# 3. 자바와 달리, private 은 없고 모든 멤버가 다 public

