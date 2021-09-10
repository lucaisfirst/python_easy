# #print 함수 연습
# print(50)
# print("50")

# a = 3
# b = 4
# print(a, a + b)

# # print
# print("%d" % 50)
# print("%f" % 3.14)
# print("%s" % "파이썬")
# print("%d %f" % (30, 3.14))
# print("%d %f %s" % (30, 3.14, "파이썬"))
# print(float(3))

# # 실수의 소수점 자리수 출력
# print("%f" % 3.141592)
# print("%.2f" % 3.1415)
# print("%08.2f" % 3.141)

# # format 함수를 이용한 서식 설정
# print("%d %3d %5d" % (123, 456, 789))
# print("{0:d} {1:3d} {2:5d}".format(123, 456, 789))
# print("{2:d} {1:3d} {0:5d}".format(123, 456, 789))

# # 부등호를 이용한 정렬
# print("{0:3d} {1:d}".format(3, 5))
# print("{0:<3d} {1:d}".format(3, 5))

# # format을 이용한 모양 만들기
# print("{0:>8s}".format("********"))
# print("{0:>8s}".format("*******"))
# print("{0:>8s}".format("******"))a
# print("{0:>8s}".format("*****"))
# print("{0:>8s}".format("****"))
# print("{0:>8s}".format("***"))
# print("{0:>8s}".format("**"))
# print("{0:>8s}".format("*"))

# # input 함수를 이용한 입출력
# num1 = input("숫자1: ")
# num2 = input("숫자2: ")
# print(num1 + num2)

# # input 함수 integer 변환
# num1 = int(input("숫자1: "))
# num2 = int(input("숫자2: "))
# print(num1 + num2)

num1 = input("숫자1: ")
num2 = input("숫자2: ")

num1 = int(num1)
num2 = int(num2)
print(num1 + num2)
