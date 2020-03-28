'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section10. 모듈과 패키지(Module&Package)
1강. 모듈(Module): 필요한 부품들을 나누어 만들어 놓은 것
'''
# 모듈 호출 방법1
import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 떄
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# 모듈 호출 방법2: 모듈에 별명을 붙여서 호출
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# 모듈 호출 방법3: 모듈명 없이 바로 사용 가능
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# 모듈 호출 방법4: 필요한 모듈만 불러서 사용 가능
from theater_module import price, price_morning
price(5)
price_morning(6)

# 모듈 호출 방법5: 필요한 모듈만 부르고, 별명 붙여서 사용
from theater_module import price_soldier as price
price(5)