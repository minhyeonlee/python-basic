# -*- coding: utf-8 -*-
'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자

Section 1. 자료형
자료형이란? 자료의 형태
숫자, 문자열, boolean
'''

#1강. 숫자 자료형
print(5)
print(-10)
print(3.13)
print(5+3)
print(2*8)
print(3*(3+1))

#2강. 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋ")
print("ㅋ"*9) #문자열을 곱할 수 있다.

#3강. Boolean(True/False) 자료형
print(5>10)
print(5<10)
print(True)
print(not True)
print(not False)
print(not (5>10))

#4강. 변수: 값을 저장하는 공간
animal = "강아지"
name = "오복이"
age = 6
hobby = "산책"
is_adult = age>=3

print("우리집 " + animal + "의 이름은 " + name + "이다.")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
print(name + "는 어른일까요? " + str(is_adult))
#+대신 ','로도 합칠 수 있으며 이 경우에는 숫자/boolean형을 str로 감싸지 않아도 된다.
print(name, "는 ", age, "이다. ", name, "은 어른일까? ", is_adult)

#5강. 주석: 코드 내에는 포함되어 있지만 실제로 실행되지 않는 것
#(1)주석처리
'''
(2)여러줄 주석처리
주석입니다.
주석~
'''