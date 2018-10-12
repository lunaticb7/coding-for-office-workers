# 구구단 만들기

dan=int(input("몇 단을 출력 하실건가요?"))

for num in range(1,10):
    print("{}*{}={}".format(dan, num, dan*num))
