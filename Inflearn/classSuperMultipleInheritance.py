'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section8. Class
'''
# 9강. super - 다중상속
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# 다중 상속(super)
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

# 다중 상속(명시적)
class FlyableUnit2(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
# 다중 상속의 경우 super을 사용하면 처음에 상속받은 클래스의 생성자만 호출된다.
# 다중 상속으로 모든 부모의 생성자를 호출하기 위해서는 모두 명시적으로 초기화해줘야 한다.
dropship = FlyableUnit()
dropship2 = FlyableUnit2()