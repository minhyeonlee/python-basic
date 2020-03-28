'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section10. 모듈과 패키지(Module&Package)
7강. 내장 함수(Built-in Function): 내장되어 따로 import할 필요 없이 사용 가능
list of python builtins를 통해 파이썬의 내장 함수를 확인할 수 있다.
'''
# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다.".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())
# random 함수에서 사용할 수 있는 것 보여줌
print(dir(random))

lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name))