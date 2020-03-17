'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section3. 문자열 처리
'''

# 1강. 문자열
# ''와 ""은 모두 문자열이다.
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
#여러줄을 저장해서 출력할 수 있다.
sentence3 = '''
나는 소년이고, 
파이썬은 쉬워요
'''
print(sentence3)

# 2강. 슬라이싱
idnumber = "990120-1234567"
print("성별: " + idnumber[7]) # 1
print("연: " + idnumber[0:2]) # 0 부터 2 직전까지 (0, 1에 있는 값 가져옴)
print("월: " + idnumber[2:4]) # 01
print("일: " + idnumber[4:6]) # 21
print("생년월일: " + idnumber[:6]) # 처음부터 6번째 직전까지
print("뒤 7자리: "+ idnumber[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에서부터): " + idnumber[-7:]) # 맨 뒤에서 7째부터 끝까

# 3강. 문자열처리함수
python = "Python is Amazing"
print(python.lower()) # 소문자 출력
print(python.upper()) # 대문자 출력
print(python[0].isupper()) # python[0]의 문자가 대문자인지 확인, True/False로 리턴
print(len(python)) # 문자열 길이 반환
print(python.replace("Python", "Java")) # 문자열을 찾은 후 다른 문자열로 바꾼다.

index = python.index("n") # 해당 문자열이 어느 위치에 있는지 찾아줌
print(index)
index = python.index("n", index+1) # 아까 찾은 n(5에 위치) 이후 부터 검색한다.
print(index)

print(python.find("n")) # index 처럼 검색해준다.
print(python.find("Java")) # 원하는 문자가 없을 경우 -1을 반환
#print(python.index("Java"))를 쓰면 오류

print(python.count("n")) # 해당 문자열이 몇 개 들어있는지 검색


# 4강. 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # %d: 정수 값
print("나는 %s을 좋아해요." % "파이썬") # %s: string 값, 정수도 출력 할 수 있다.
print("Apple은  %c로 시작해요." % "A") # %c: char(문자 1개) 값
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=30, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=30))

# 방법 4(v3.6이상 부터 가능)
age = "20"
color ="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 5강. 탈출문자
# \n: 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \': 문장 내에서 따옴
# 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\: 문장 내에서 \(경로 출력 등에 사용)
print("C:\\User\\Desktop")

# \r: 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b: 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t: 탭
print("Red\tApple")
