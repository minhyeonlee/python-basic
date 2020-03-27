'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section9. 예외처리(Exception Handling)
'''
#1강. 예외처리: 에러가 발생했을 때 처리
# 한글이 입력되면 오류가난다. -> 예외처리
# 0으로 나누면 오류가난다. -> 예외처리(ZeroDivisionError)
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err) # list index out of range
