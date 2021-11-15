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

# # 2차원 리스트(길이가 다른 리스트)
# list2 = [["김범석", 6, 10, 20, 30, 50], ["허림", 5, 90, 90, 100],
#          ["이승형", 3, 100], ["홍길동", 4, 90, 60]]

# total = 0
# ave = 0

# for i in range(0, 4, 1):
#     for j in range(2, list2[i][1], 1):
#         total = total + list2[i][j]
#     ave = total / (list2[i][1]-2)
#     list2[i].insert(2, ave)
#     list2[i][1] = list2[i][1] + 1  # 변화한 길이정보 업데이트
#     total = 0

# for i in range(0, 4, 1):
#     for j in range(0, list2[i][j], 1):
#         if j == 0:
#             print("%s" % list2[i][j], end="")
#         elif j == 1:
#             print("", end="")
#         elif j == 2:
#             print("%6.1f" % list2[i][j], end="")
#         else:
#             print("%d" % list2[i][j], end="")
#     print("\n")

# 빙고게임
bingoList = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
    11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
redundantList = []
bingo = False

while(bingo == False):
    userNum = int(input())
    if userNum < 1 or userNum > 25:
        continue
    elif redundantList.count(userNum) > 0:
        continue
    else:
        redundantList.append(userNum)

        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                if userNum == bingoList[i][j]:
                    bingoList[i][j] = 0

        rowFlag = 0
        colFlag = 0
        LCrossFlag = 0
        RCrossFlag = 0

        for i in range(0, 5, 1):
            rowFlag = 0
            colFlag = 0
            for j in range(0, 5, 1):
                if bingoList[i][j] == 0:
                    rowFlag = rowFlag + 1
                if bingoList[j][i] == 0:
                    colFlag = colFlag + 1
            if rowFlag == 5 or colFlag == 5:
                bingo = True
                break

            if bingoList[i][j] == 0:
                LCrossFlag = LCrossFlag + 1
            if bingoList[4 - i][j] == 0:
                RCrossFlag = RCrossFlag + 1

        if LCrossFlag == 5 or RCrossFlag == 5:
            bingo = True
            break

    for i in range(0, 5, 1):
        for j in range(0, 5, 1):
            print("%3d" % bingoList[i][j], end="")
        print("\n")

print("Bingo")
