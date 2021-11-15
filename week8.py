list1 = ["김하진", 50, 100, 100, 80]
list2 = ["허림", 90, 88, 95, 100]
list3 = ["이승형", 100, 100, 100, 100]
list4 = ["홍길동", 10, 20, 30, 40]

total = 0
ave = 0

for i in range(1, 5, 1):
    total = total + list1[i]
ave = total / 4
list1.insert(1, ave)
total = 0

print(list1)

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
