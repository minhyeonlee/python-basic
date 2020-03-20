"""
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section5.

Quiz)표준 체중을 구하는 프로그램을 작성하시오.
* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
 남자 : 키(m) X 키(m) X 22
 여자 : 키(m) X 키(m) X 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""
height, gender = input().split()
height = int(height)

def std_weight(height, gender): # 키 m 단위 (실수), 성 "남자"/"여자"
    if(gender=="여자"):
        weight = height * height * 22
        return weight
    else:
        weight = height * height * 22
        return weight

weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
