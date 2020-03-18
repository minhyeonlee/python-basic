'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section4. Data Structure(자료구조)
4강. 집합(set): 중복이 안되고, 순서가 없다.
'''
my_set = {1,2,3,3,3}
print(my_set) # 1,2,3만 출력된다.

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java, python을 모두 할 수 있는 개발자)
print(java&python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java|python)
print(java.union(python))

# 차집합 (java는 할 줄 알지만 python을 못하는 개발자)
print(java-python)
print(java.difference(python))

# 값 추가하기: python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 값 지우기: java를 잊어버렸어요.
java.remove("김태호")
print(java)