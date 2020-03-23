'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section8. Class
'''
# 5강. 상속(Class Inheritance): 물려 받는 것을 의미
# 일반 유닛을 상속 받아서 Attack 유닛을 만들어보자.
# 일반 유닛
# 메딕 : 의무병(공격력이 없다)
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


# 파이어뱃, 공격, 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
# 공격함
firebat1.attack("5시")
# 공격 받음음
firebat1.damaged(25)
firebat1.damaged(25)
