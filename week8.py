# # 1차원 리스트
# list1 = ["김하진", 50, 100, 100, 80]
# list2 = ["허림", 90, 88, 95, 100]
# list3 = ["이승형", 100, 100, 100, 100]
# list4 = ["홍길동", 10, 20, 30, 40]

# total = 0
# ave = 0

# for i in range(1, 5, 1):
#     total = total + list1[i]
# ave = total / 4
# list1.insert(1, ave)
# total = 0

# print(list1)

# for i in range(1, 5, 1):
#     total = total + list2[i]
# ave = total / 4
# list2.insert(1, ave)
# total = 0

# print(list2)

# for i in range(1, 5, 1):
#     total = total + list3[i]
# ave = total / 4
# list3.insert(1, ave)
# total = 0

# print(list3)

# for i in range(1, 5, 1):
#     total = total + list4[i]
# ave = total / 4
# list4.insert(1, ave)
# total = 0
# print(list4)

# # 2차원 리스트
# list2 = [["김하진", 50, 100, 100, 80], ["허림", 90, 88, 95, 100],
#          ["이승형", 100, 100, 100, 100], ["홍길동", 10, 20, 30, 40]]

# total = 0
# ave = 0

# for i in range(0, 4, 1):
#     for j in range(1, 5, 1):
#         total = total + list2[i][j]
#     ave = total / 4
#     list2[i].insert(1, ave)
#     total = 0
#     print(list2[i])

# 2차원 리스트(길이가 다른 리스트)
# list2 = [["김하진", 6, 50, 100, 100, 80], ["허림", 5, 90, 88, 95],
#          ["이승형", 3, 100], ["홍길동", 4, 90, 40]]

# for i in range(0, 4, 1):
#     for j in range(2, list2[i][1], 1):
#         total = total[i][j]
#     ave = total / (list[i][1]-2)
#     list2[i].insert(2, ave)
#     list2[i][1] = list2[i][1] + 1
#     total = 0

list2 = [["김하진", 6, 50, 100, 100, 80], ["허림", 5, 90, 88, 95],
         ["이승형", 3, 100], ["홍길동", 4, 90, 40]]

total = 0
ave = 0

for i in range(0, 4, 1):
    for j in range(2, list2[i][1], 1):
        total = total + list2[i][j]
    ave = total / (list2[i][1]-2)
    list2[i].insert(2, ave)
    list2[i][1] = list2[i][1] + 1  # 변화한 길이정보 업데이트
    total = 0

for i in range(0, 4, 1):
    for j in range(0, list2[i][j], 1):
        if j == 0:
            print("%s" % list2[i][j], end="")
        elif j == 1:
            print("", end="")
        elif j == 2:
            print("%6.1f" % list2[i][j], end="")
        else:
            print("%3d" % list2[i][j], end="")
    print("\n")
