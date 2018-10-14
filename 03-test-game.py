#사용자에게 가위, 바위, 보 중 하나를 물어 본다.
#사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위 바위,보를 내고 승패를 가른다.
#다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 난다.
#리스트를 한 개 사용하고 사용자의 입력 받아야 한다.
#임의 뽑기 다시 사용.
#컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 한다.

import random

win_count =0
lose_count = 0

print("가위, 바위, 보 게임을 시작해요!")
print("3승을 하면 이기게 되고, 3패를 하면 지게 되요.")
print("종료하고 싶으면 종료라고 입력해주세요.")

while (win_count<3 and lose_count<3):
    person = ("가위", "바위", "보")
    computer = random.choice(person)
    player = None
    while (player not in person):
        player = input("가위, 바위, 보 중 하나를 내십시오 : ")
        if player == "종료":
            print("가위, 바위, 보 게임을 종료하겠습니다.")
            exit()
    print("당신은 {}를 내셨습니다.".format(player))
    print("컴퓨터는 {}를 냈습니다.".format(computer))

    if player == computer:
        print("비겼습니다.\n")
        print("{}승 {}패 입니다.".format(win_count, lose_count))

    #player가 바위 냈을 때
    elif player =="바위" and computer =="보":
        print("당신은 졌습니다.\n")
        lose_count+=1
        print("{}승 {}패 입니다.".format(win_countm,lose_count))
    elif player =="바위" and computer =="가위":
        print("당신은 이겼습니다.\n")
        win_count+=1
        print("{}승 {}패 입니다.".format(win_count, lose_count))

    #player가 가위 냈을 때
    elif player =="가위" and computer =="보":
        print("당신은 이겼습니다.\n")
        win_count+=1
        print("{}승 {}패 입니다.".format(win_count, lose_count))
    elif player =="가위" and computer =="바위":
        print("당신은 졌습니다.\n")
        lose_count+=1
        print("{}승 {}패 입니다.".format(win_count, lose_count))

    #player가 보 냈을 때
    elif player =="보" and computer =="가위":
        print("당신은 졌습니다.\n")
        lose_count+=1
        print("{}승 {}패 입니다.".format(win_count, lose_count))
    elif player =="보" and computer =="바위":
        print("당신은 이겼습니다.\n")
        win_count+=1
        print("{}승 {}패 입니다.".format(win_count, lose_count))

if(win_count):
    print("최종적으로 당신이 이겼습니다. 축하드립니다.")
if(lose_count):
    print("최종적으로 컴퓨터가 이겼습니다. 다시 해서 컴퓨터를 이겨보세요.")
