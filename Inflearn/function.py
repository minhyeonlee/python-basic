'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section5. Function(함수)
'''
# 1강. 함수(함수를 정의 해 놓고 호출하기 전까지는 실행되지 않는다.)
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 2강. 전달 값과 반환 값
def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return  balance + money

def withdraw(balance, money): #출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금(수수료가 있다)
    commission = 100 # 수수료 100원
    return commission, balance - money - commission #튜플 형식으로 여러개의 값 반환

balance = 0 # 잔액
balance = deposit(balance, 1500)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))