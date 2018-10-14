#한식, 일식, 중식 중 고르라는 메세지
#한가지를 고르면 식당 이름을 하나 임의로 추천
#리스트를 여러개 사용하고 사용자의 입력을 받아야 함.

type = input("한식, 일식, 중식 중 선택해 주세요.")

korean=["김밥천국", "사계"]
japanese=["시부야", "도쿄"]
chinese=["왕서방", "북경"]


if type == "한식":
    import random
    korea=random.choice(korean)
    print(korea)
elif type == "일식":
    import random
    japan=random.choice(japanese)
    print(japan)
elif type == "중식":
    import random
    china=random.choice(chinese)
    print(china)
