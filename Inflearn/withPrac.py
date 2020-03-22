'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section7. Input and Output(입출력)
'''
# 5강. with: close를 해줄 필요가 없다.
import pickle
# pickle 파일을 불러와서 profile_file에 저장
# pickle.load를 통해 출력
# with문을 탈출하면서 자동으로 close해주므로 따로 close문을 사용할 필요가 없다.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# with로 일반 파일쓰기
with open("study.txt", "w", encoding="utf") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

# with 일반 파일읽기
with open("study.txt", "r", encoding="utf") as study_file:
    print(study_file.read())