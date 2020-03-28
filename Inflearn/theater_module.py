'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section10. 모듈과 패키지(Module&Package)
1강. 모듈(Module): 필요한 부품들을 나누어 만들어 놓은 것
'''
# 모듈 파일
# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 100000))

# 조조 할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))
