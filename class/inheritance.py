# 클래스의 상속
# class 클래스명(부모클래스)
# > 이렇게하면 부모 클래스의 내용을 상속받아 사용할 수 있다.
class add_calculator:
    def addition(self, x, y):
        return x + y


class good_calculaotr(add_calculator):
    def substraction(self, x, y):
        return x - y


calc1 = add_calculator()
print(calc1.addition(3, 4))
calc2 = good_calculaotr()
print('calc2 : ', calc2.addition(3, 4))
print('calc2 : ', calc2.substraction(3, 4))


# super() 를 사용하면 부모에게 정의된 함수를 불러올 수 있다.
class super_calculator(add_calculator):
    # 부모의 메소드와 이름이 똑같은 메소드를 자식에게 정의하면 오버라이딩 된다.
    # 즉, 부모의 addition 의 내용이 아래와 같이 변경되는 것. 부모의 addition 은 더 쓸 수 없다.
    def addition(self, x, y):
        print('calc 3 : ', super().addition(x, y))
        print('one more')
        print('calc 3 : ', super().addition(x, y))

calc3 = super_calculator()
calc3.addition(3, 4)




