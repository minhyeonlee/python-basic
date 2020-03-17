'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section3.
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

예) http://naver.com
규칙1: http://부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

예) 생성된 비밀번호: nav51!
'''
url = "http://naver.com"

# 규칙1: http://를 제외한다.
my_str = url.replace("http://", "")

# 규칙2: 처음 만나는 점(.) 이후 부분 제외
my_str = my_str[:my_str.index(".")]

# 규칙3:
char = my_str[:3]
length = len(my_str)
cnt = my_str.count('e')
pwd = char+str(length)+str(cnt)+"!"

print("{0} 의 비밀번호는 {1} 입니다.".format(url, pwd))