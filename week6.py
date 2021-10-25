# # 예제 1
# while input() != 'q':
#     print("q이외에 다른 문자가 입력됨")
# else:
#     print("q가 입력되어 종료됩니다. ")

# # 예제 2
# while True:
#     myin = input()
#     if myin == 'q':
#         print('q가 입력되어 종료합니다.')
#         break
#     print("%s가 입력되었습니다." % myin)

# # 예제 3
# num = int(input())
# while num > 10:
#     print(num)
#     num -= 1
# else:
#     print("num이 10보다 작은 수 입니다.")

# # 예제 4 1부터 10까지 합 구하는 것
# sum = 0
# for i in range(1, 11, 1):
#     sum += i
#     if(i < 10):
#         print("%d +" % i, end="")
#     else:
#         print("%d =" % i, end="")

# print(sum)

# # 예제 5 while문으로 한다.
# sum = 0
# i = 1
# while i <= 10:
#     sum += i
#     if(i < 10):
#         print("%d +" % i, end="")
#     else:
#         print("%d =" % i, end="")
#     i += 1
# print(sum)

# 예제 6 사칙연산 프로그램
while True:
    while True:
        tmp1 = input("첫번째 수를 입력 : ")
        if(tmp1.isdigit()):
            num1 = int(tmp1)
            break
        else:
            print("숫자를 입력하세요.")
    while True:
        tmp2 = input("두번째 수를 입력 : ")
        if(tmp2.isdigit()):
            num2 = int(tmp2)
            break
        else:
            print("숫자를 입력하세요.")
    while True:
        tmp3 = input("연산자(+, -, *, /)를 입력: ")

        if tmp3 == '+' or tmp3 == '-' or tmp3 == '*' or tmp3 == '/' or tmp3 == 'q' or tmp3 == '0':
            oper = tmp3
            break
        else:
            print("+, -, *, /, 0, q를 입력하세요.")

    if oper == '0' or oper == 'q':
        break
    elif oper == '+':
        print("%d + %d = %d" % (num1, num2, num1+num2))
    elif oper == '-':
        print("%d - %d = %d" % (num1, num2, num1-num2))
    elif oper == '*':
        print("%d * %d = %d" % (num1, num2, num1*num2))
    elif oper == '/':
        print("%d / %d = %d" % (num1, num2, num1/num2))
