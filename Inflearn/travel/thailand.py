'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section10. 모듈과 패키지(Module&Package)
'''
# 2강. Thailand 패키지(Package) 작성
class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

# 4강. 모듈 직접 실행
# 개발자가 모듈을 테스트 하기 위해 사용
# thailand.py에서 직접 실행 했을 때 이 구문을 타게된다.
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")