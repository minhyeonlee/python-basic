'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section7. Input and Output(입출력)
'''
# 4강. pickle
import pickle
# pickle 파일에 데이터 저장
profile_file = open("profile.pickle", 'wb') # wb: write binary: pickle을 사용하기 위해 binary 형식으로 저장
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "야구"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

# pickle 파일 읽어오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 저장
print(profile)
profile_file.close()