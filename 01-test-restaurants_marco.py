import random

#1)리스트를 만든다
KOREAN_FOOD = ("김치찌개", "비빔밥", "국수")
CHINESE_FOOD = ("짱장면", "탕수육", "짬뽕")
JAPANESE_FOOD = ("라멘", "돈까스", "돈부리")

#2)사용자로부터 입력
user_choice = input("한식, 중식, 일식 중에서 골라주세요:")

#3)임의로 추천
if user_choice == "한식":
    choice_result = random.choice(KOREAN_FOOD)
    #choice_result = random.randint(0, len(KOREAN_FOOD))
elif user_choice == "중식":
    choice_result = random.choice(CHINESE_FOOD)
elif user_choice == "일식":
    choice_result = random.choice(JAPANESE_FOOD)
else:
    print("한식, 중식, 일식 중에서 선택하셔야 합니다.")

if choice_result:
    print("{}중에서 {}이 선택 되었습니다.".format(user_choice, choice_result))
