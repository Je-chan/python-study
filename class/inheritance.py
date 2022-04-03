class add_calculator:
    def addition(self, x, y):
        return x + y


class good_calculaotr(add_calculator):
    def substraction(self, x, y):
        return x - y


calc1 = add_calculator()
print(calc1.addition(3, 4))
calc2 = good_calculaotr()
print(calc2.addition(3, 4))
print(calc2.substraction(3, 4))
