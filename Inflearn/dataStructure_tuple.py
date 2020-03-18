'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section4. Data Structure(자료구조)
3강. 튜플(tuple): 리스트(list)와 다르게 내용 변경/추가가 불가능하다.
하지만 속도가 리스트보다 빠르다. 변경되지 않는 값에 많이 사용한다.
'''
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

#서로 다른 변수에 서로 다른 값을 한 번에 저장 가능
(name2, age2, hobby2) = ("유재석", 30, "singing")
print(name2, age2, hobby2)

