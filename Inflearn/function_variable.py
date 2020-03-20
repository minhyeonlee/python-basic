'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section5. Function(함수)
'''
# 6강. 지역변수와 전역변수(Local Variable, Global Variable)
# 지역변수(Local Variable): 함수 내에서만 사용(함수가 호출될 떄 만들어지고 함수가 끝나면 사라짐)
# 전역변수(Global Variable : 프로그램이 끝날 때 까지 사용 가능)

gun = 10
gun2 = 10

# 전역변수 사용하는 함수 (잘 사용하지 않음)
def checkpoint(soliders): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))

# 전역변수를 인자로 받고 리턴 값을 돌려주는 함수
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총(2) : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

print("전체 총(2) : {0}".format(gun2))
gun2 = checkpoint_ret(gun2, 2)
print("남은 총(2) : {0}".format(gun2))




