'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section8. Class
'''
# 3강. Class 멤버 변수(Member Variable)
# Member Variable : 클래스 내에서 정의된 변수(self.name, self.hp 등)
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 {1}".format(self.hp, self.damage))

#marine1 = Unit("마린", 40, 5)
#marine2 = Unit("마린", 40, 5)
#tank = Unit("탱", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# 객체 이름.변수명(클래스 내의 멤버변수에 접근이 가능하다)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
# clocking 변수는 Unit내에 없다. 외부에서 추가로 할당함
# 추가로 외부 변수를 만들어 사용할 수 있다.(확장이 가능하고 내가 외부 변수를 할당한 객체에만 적용된다.)
# wraith1의 멤버 변수 : name, hp, damage
# wraith2의 멤버 변수 : name, hp, damage, clocking
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))