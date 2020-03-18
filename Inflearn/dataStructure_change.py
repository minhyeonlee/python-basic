'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section4. Data Structure(자료구조)
5강. 자료구조의 변경(Change of data structure)
'''
# 커피 메뉴 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # 집합 형태이므로  type(menu): class 'set'출력 {}

menu = list(menu)
print(menu, type(menu)) # 자료의 형태가 list로 변경: class 'list' []

menu = tuple(menu)
print(menu, type(menu)) # 자료의 형태가 tuple 변경: class 'tuple' ()

menu = set(menu)
print(menu, type(menu)) # 다시 set로 변경