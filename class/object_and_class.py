# Class 의 이름을 먼저 정의
class human:
    # Class 가 처음 호출될 떄 실행될 method
    def __init__(self, height, age):
        # Class 의 변수
        self.height = height
        self.age = age

    # Class 의 메소드: 첫 번째 매개변수로 자기 자신을 갖는다.
    def how_old(self):
        print(self.age, "살 입니다.")

    def how_tall(self):
        print(self.height, "cm 입니다.")

    def greeting(self, param1, param2):
        print(param1)
        print(param2)


je = human(184, 28)
print(je.age)
print(je.height)

je.age = 26
print(je.age)
je.position = "front-end"
print(je.position)

je.how_old()
je.how_tall()
je.greeting('첫 번째, 안녕', '두 번째, hi')

liebe = human(183, 25)
print(liebe.age)

# 동일한 클래스를 사용하더라도 인스턴스끼리는 다른 메모리를 차지하므로, 같지 않다.
print(je == liebe)