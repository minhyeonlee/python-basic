'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section7. Input and Output(입출력)
'''
# 3강. 파일 입출력(File I/O)

# 파일 쓰기
# score.txt가 생긴다.
score_file = open("score.txt", "w", encoding="utf8") # w: write
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 파일 이어쓰기
score_file = open("score.txt", "a", encoding="utf8") # a: append(만약 w를 하면 파일이 덮어써진다.)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # 줄바꿈을 명시적으로 해줘야함
score_file.close()

# 파일 읽기
score_file = open("score.txt", "r", encoding="utf8") # r: read
print(score_file.read())
score_file.close()

# 파일 한줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기 동작, 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print()
score_file.close()

# 파일 전체 읽기(몇 줄인지 모를 때)
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # line에 내용이 없을 경우
        break
    print(line, end="")
print()
score_file.close()


# 파일 읽기(리스트에 값 넣은 후 처리)
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
