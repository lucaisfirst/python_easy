# # 리스트 인덱스
# arr = [2, 4, 6, 8, 10]
# print(arr)

# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])

# # 리스트 연산자
# arr1 = [2, 4, 6, 8]
# arr2 = [10, 12, 14, 16]
# arr3 = arr1 + arr2
# print(arr3)

# arr1 = [2, 4, 6, 8]
# arr2 = arr1*3
# print(arr2)

# arr1 = [2, 4, 6, 8]
# print(4 in arr1)
# print(10 in arr1)
# length = len(arr1)
# print(length)

# arr1 = [2, 4, 6, 8]
# arr1.append(10)
# print(arr1)

# arr1 = [2, 4, 6, 8]
# arr2 = [10, 12]
# arr1.extend(arr2)
# print(arr1)

# arr1 = [2, 4, 6, 8]
# arr1.insert(2, 5)
# print(arr1)

# # 리스트 함수
# arr1 = [10, 20, 30, 40, 50]
# num = arr1.pop()
# print(arr1)
# print(num)

# arr1 = [10, 20, 30, 42, 50]
# num = arr1.pop(2)
# print(arr1)
# print(num)

# arr1 = [10, 20, 30, 40, 50]
# arr1.remove(20)
# print(arr1)

# # 예제1
# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 2, 3, 4, 5]

# if len(list1) != len(list2):
#     print("두 리스트는 같지 않습니다.")
# else:
#     flag = 0

#     for i in range(len(list1)):
#         flag = 1
#         break
#     if flag == 1:
#         print("두 리스트는 같지 않습니다.")
#     else:
#         print("두 리스트는 같습니다.")

# 예제2
ageList = [10, 2, 0, 10, 0, 60, 90, 42, 12, 42, 10, 0, 1]

countList = [0]

for i in range(0, 100, 1):
    countList.append(0)

for i in range(0, 20, 1):
    countList[ageList[i]] = countList[ageList[i]] + 1

for i in range(0, 101, 1):
    if countList[i] != 0:
        print("%d세, %d명" % (i, countList[i]))


# 예제3
searchList = [2, 43, 53, 53, 52, 65, 4, 64, 35]
key = 12

index = -1

length = len(searchList)

for i in range(0, length, 1):
    if key == searchList[i]:
        index
