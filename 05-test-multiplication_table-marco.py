#사용자가 다른 값을 넣더라도 에러가 나지 않도록 처리
#2~9단 까지만 처리
#예로 1단 넣으면 구구단이 실행되지 않고 종료
#잘못된 값을 입력한 경우, "2에서 9사이의 숫자만 입력 해 주세요." 라는 문구화 함께 구구단 다시 실행

def gugudan():
    try:
        dan = int(input("2에서 9사이의 숫자를 입력해주세요: "))
        if dan > 1 and dan < 9:
            for num in range (2, 10):
                print("{} * {} = {}".format(dan, num, dan*num))
        else:
            print("2에서 9사이의 숫자만 입력해주세요!!")
            gugudan()
    except ValueError:
        print("숫자만 입력해주세요.")
        gugudan()
    except:
        print("알 수 없는 오류가 발생했습니다.")
        gugudan()
gugudan()
