'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section4. Data Structure(자료구조)
2강. 사전(dictionary): key와 value로 구
'''
cabinet = {3:"유재석", 100:"김태호"}
# 사전에서 값 가져오기1: dicName[key](사전에 없는 키 값을 적으면 오류가 발생)
print(cabinet[3])
print(cabinet[100])

# 사전에서 값 가져오기2: get(key)(사전에 없는 키 값을 적으면 None값 출력)
# None말고 default 값도 출력이 가능하다.
print(cabinet.get(3))
print(cabinet.get(5, "사용가능"))

# 사전에서 키 값의 유무 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

# key 값을 string으로 선언 가능
cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

# 사전에 새로운 값 넣기/업데이트: 새로운 손님이 왔을 때
print(cabinet2)
cabinet2["A-3"] = "김종국"
cabinet2["C-20"] = "조세호"
print(cabinet2)

# 값 지우기: 손님이 갔을 때
del cabinet2["A-3"]
print(cabinet2)

# key 값들만 출력
print(cabinet2.keys())

# value 값들만 출력
print(cabinet2.values())

# key, value 쌍으로 출력
print(cabinet2.items())

# 모든 값 지우기: 영업 종료
cabinet.clear()
cabinet2.clear()
print(cabinet)
print(cabinet2)


