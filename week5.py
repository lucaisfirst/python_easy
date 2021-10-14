# # 기본적인 for문
# fruit = ['apple', 'banana', 'watermelon', 'strawberry']
# for i in fruit:
#     print(i)

# # 튜플을 이용한 for문
# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first + last)

# # for문과 if문의 사용
# scores = [100, 70, 50, 25, 85]

# number = 0
# for score in scores:
#     number = number + 1
#     if score >= 70:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)


# # 예제 1
# for i in range(100):
#     print("재미있는 파이썬!")
# # 예제 2
# for i in range(100):
#     print("재미있는 파이썬!", i)
# # 예제 3
# for i in range(5, 11):
#     print("재미있는 파이썬!", i)
# # 예제 4
# for i in range(0, 11):
#     print("재미있는 파이썬!", i)
# # 예제 5
# for i in range(10, 0, -1):
#     print("재미있는 파이썬", i)

# # 예제 6
# count = int(input("반복할 수를 입력하세요: "))
# for i in range(count):
#     print("재미있는 파이썬!", i)
# # 예제 7
# n = 5
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)
# # 예제 8
# print("구구단 출력")
# for i in range(2, 10):
#     print('')
#     for j in range(1, 10):
#         print('%d * %d = %d' % (i, j, i*j))
# # 예제 9
# int(input("출력할 단어를 입력하세요.: "))
# print("구구단 출력")
# for i in range(1, 10):
#     print("%d * %d")

# # 예제 10
# for a in range(0, 10):
#     for i in range(a+1):
#         print("*", end="")
#     print()

# for a in range(0, 10):
#     print("*"*(a+1))
# # 예제 11
# for a in range(10, 0, -1):
#     for i in range(a-1):
#         print("*", end="")
#     print()
# for b in range(0, 10):
#     print("{:>10}".format("*"*(b+1)))

# 예제 12


# -1시간 24분에서 하차함. 다시 들어야 됨
