'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section8. Class
'''
# 6강. 다중 상속(Multiple Inheritance) :2개 이상의 부모 클래스를 상속 받는다.
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp



# 공격 유닛 : 일반 유닛 클래스를 상속 받음
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # name, hp를 정의해줄 필요가 없고 생성자를 통해 이름과 체력을 초기화 할 수 있다.
        Unit.__init__(self, name, hp)
        self.damage = damage

    # 공격 함수
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
              .format(self.name, location, self.damage))

    # 공격 받은 함수
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if(self.hp<=0):
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽: 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 불가

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스(다중 상속)
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")