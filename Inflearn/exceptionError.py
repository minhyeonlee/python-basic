'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section9. 예외처리(Exception Handling)
'''
#2강. 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise  ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

