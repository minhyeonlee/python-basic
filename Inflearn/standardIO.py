'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section7. Input and Output(입출력)
'''
# 1강. 표준 입출력(standard input/output)
print("Python" + "Java") # PythonJava
print("Python", "Java") # Python Java
print("Python", "Java", "JavaScript", sep=" vs ") # Python vs Java vs JavaScript
print("Python", "Java", sep=",", end="?") # end함수를 명시적으로 적을 경우 아래 문장과 함께 한 줄에 출력된다.
print("무엇이 더 재밌을까요?") # Python,Java?무엇이 더 재밌을까요?

import sys
print("Python", "Java", file=sys.stdout) # stdout: TextIO(표준 입출력)
print("Python", "Java", file=sys.stderr) # stderr: 에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100} # dictionary
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8): 8자 공간을 확보 후 왼쪽정렬, rjust: 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 20):
    print("대기번호 : " + str(num).zfill(3)) # zfill(0을 n번만큼 채움)

# 표준 입력
answer = input("아무 값이나 입력하세요 : ") # input값은 항상 string 값으로 저장된다.
print("입력하신 값은 " + answer + "입니다.")


