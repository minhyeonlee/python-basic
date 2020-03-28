'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section10. 모듈과 패키지(Module&Package)
5강. 패키지, 모듈 위치
우리가 만들 모듈을 random 모듈이 있는 위치에 넣고 실행해본다.
다른 프로젝트를 할 때에도 사용이 가능해진다.
'''
import inspect
import random
from travel import *
print(inspect.getfile(random))
print(inspect.getfile(thailand))
