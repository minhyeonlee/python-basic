'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section8. Class
'''
# 2강. Class Init: init은 python에서 쓰이는 생성자이다.
# 객체 생성시 자동으로 호출되는 부분이다.(객체: class로 만들어지는 것)
# marine, tank 등은 인스턴스라고 한다.
# 객체 생성시 init에 정의된 arguments와 동일한 수의 인자를 던저준다.(self 제외)
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱", 150, 35)