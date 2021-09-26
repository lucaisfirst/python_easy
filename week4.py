# 1번째 강의 이론
# print("시험에 응시하시겠습니까? 응시:1 미응시: 1이 아닌 수")
# flag = int(input())

# if flag == 1:
#     print("시험에 응시하였습니다.")
#     print("점수를 입력해주세요.")
#     score = int(input())

#     if score > 100 or score < 0:
#         print("점수를 잘못 입력하셨습니다. 점수의 크기는 0보다 크거나 작고, 100보다 작거나 같습니다.")
#     elif score >= 90:
#         print("점수는 A")
#     elif score >= 80:
#         print("점수는 B입니다.")
#     elif score >= 70:
#         print("점수가 C입니다.")
#     elif score >= 60:
#         print("점수가 C입니다.")
#     else:
#         print("점수가 F입니다.")
# else:
#     print("시험에 결시하였습니다.")

# # 2번째 강의 실습1: 사칙연산 계산기
# num1 = int(input("첫 번째 값을 입력해주세요: "))
# num2 = int(input("두 번째 값을 입력해주세요: "))
# op = input("연산자를 입력하세요(+, -, *, /): ")

# if op == "+":
#     result = num1 + num2
#     print(result)
# elif op == "-":
#     result = num1 - num2
#     print(result)
# elif op == "*":
#     result = num1 * num2
#     print(result)
# elif op == "/":
#     result = num1 / num2
#     print(result)
# else:
#     print("잘못된 연산자를 입력하셨습니다.")

# # 실습 2: 최대 최소
# a = int(input())
# b = int(input())
# c = int(input())

# if a > b:
#     if a > c:
#         max = a
#         if b > c:
#             min = c
#         else:
#             min = b
#     else:
#         max = c
#         min = b
# else:
#     if b > c:
#         max = b
#         if a > c:
#             min = c
#         else:
#             min = a
#     else:
#         max = c
#         min = a
# print(max)
# print(min)

# # 주민번호
# jumin = input("주민번호를 입력하세요.(xxxxxx-xxxxxxx): ")
# birth, disting = jumin.split("-")

# year = int(birth[0:2])
# month = int(birth[2:4])
# day = int(birth[4:6])

# gender = int(disting[0])

# if gender == 3:
#     print("%02d년 %d월 %d일, 남성" % (year, month, day))
# else:
#     print("%02d년 %d월 %d일, 여성" % (year, month, day))

# # 예제 3: 큰 수 찾기
# num1 = int(input())
# num2 = int(input())

# if num1 > num2:
#     max = num1
#     min = num2
# else:
#     max = num2
#     min = num1

# differ = max - min
# print(differ)

# # 예제 4: 큰 수 찾기
# num1 = int(input())
# num2 = int(input())

# if num1 > num2:
#     max = num1
#     min = num2
# else:
#     max = num2
#     min = num1

# if max % min == 0:
#     print("약수")
# else:
#     print("약수가 아님")

# 예제 5: 가위바위보 게임
player1 = input("player1님 '가위, 바위, 보'에서 골라: ")
player2 = input("player2님 '가위, 바위, 보'에서 골라: ")

if player1 == "가위":
    if player2 == "가위":
        print("비겼습니다.")
    elif player2 == "바위":
        print("player2가 이겼습니다.")
    else:
        print("player1이 이겼습니다.")
if player1 == "바위":
    if player2 == "바위":
        print("비겼습니다.")
    elif player2 == "보":
        print("player2가 이겼습니다.")
    else:
        print("player1이 이겼습니다.")
if player1 == "보":
    if player2 == "보":
        print("비겼습니다.")
    elif player2 == "가위":
        print("player2가 이겼습니다.")
    else:
        print("player1이 이겼습니다.")
