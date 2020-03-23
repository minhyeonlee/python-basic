'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section8. Class
'''
# 4강. Class Method
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 {1}".format(self.hp, self.damage))

class AttackUnit:
    # self는 자기 자신을 의미(클래스 내에서 메소드 앞에는 항상 self를 써줌)
    def __init__(self, name, hp, damage):
        # 뒤의 그냥 name, hp, damage는 전달 받은 값
        self.name = name
        self.hp = hp
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