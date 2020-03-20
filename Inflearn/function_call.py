'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section5. Function(함수)
'''
# 3강. 기본값: 함수에 기본 값을 설정해서 인자가 들어오지 않았을 경우 기본 값을 출력한다.
# \+Enter 띄어쓴 두 문장을 한 문장으로 인식한다.
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
# 값을 전달받지 않으면 기본 값을 출력한다.
def profile2(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile2("유재석")
profile2("김태호")

# 4강. 키워드값: 키워드 값을 통해 인자를 전달한다.
def profile3(name, age, main_lang):
    print(name, age, main_lang)

profile3(name="유재석", main_lang="파이썬", age=20)
profile3(main_lang="자바", age=25, name="김태호", )

# 5강. 가변인자를 통한 함수 호출
def profile4(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    print(lang1, lang2, lang3, lang4, lang5)

# 기존 함수 profile4는 lang가 5개 이상, 또는 5개 미만일 경우 함수를 바꾸거나 빈칸을 넣어줘야함.
profile4("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile4("김태호", 25, "Kotlin", "Swift", "", "", "")

# 가변 인자를 통한 함수(인자의 개수가 달라더 같은 함수를 쓸 수 있다)
def profile5(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    for lang in language:
        print(lang, end=" ")
    print()

profile5("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile5("김태호", 25, "Kotlin", "Swift")