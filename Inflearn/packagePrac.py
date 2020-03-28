'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section10. 모듈과 패키지(Module&Package)
'''
# 2강. 패키지(Package): 하나의 디렉토리에 모듈 파일들을 모아 놓은 것
# class나 function은 바로 import를 할 수 없다.
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from import에서는 class, function 바로 호출 가능
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# 3강. __all__
# 이렇게 사용하면 에러가 난다.(개발자가 패키지에서 import되기를 원하는 것만 공개할 수 있음)
# __init__파일 수정 후 정상 동작
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()
