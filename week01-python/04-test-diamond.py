#for loop
# 00100
# 01110
# 11111
# 01110
# 00100
#다이아몬드를 5x5 좌표에 그릴 수 있다.
#반복문(for-loop)은 중첩해서 사용할 수 있다.

# 1
# 11
# 111
# 1111
# 11111
# for a in range(1, 6):
#     # for b in range(1,6):
#     #     print()
#     print("1" * a)

# 10000
# 11000
# 11100
# 11110
# 11111
# for a in range(1, 6):
#     print("1" * a + "0" * (5-a))

# 00100
# 01110
# 11111
# 01110
# 00100
for a in range(1, 6):
    a = a-3
    if a < 0:
        a = -a
    print("0" * a + "1" * (5 - a * 2) + "0" * a)

#1 2 3 4 5     -2 -1 0 1 2    2 1 0 1 2
