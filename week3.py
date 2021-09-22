# # 문자열 포매팅
# str = "오늘은 %d월 %d일 입니다"
# month = 3
# day = 7
# print(str % (month, day))

# # 문자열 포매팅 정렬
# str = "%10d" % 10
# print(str)
# str = "%010d" % 10
# print(str)
# str = "%10f" % 3.14
# print(str)
# str = "%10s" % "abc"
# print(str)

# # 문자열 포매팅 실습
# str = "%4d년 %2d월 %2d일, 용인시는 %2d도로 %s날씨입니다"
# year = int(input("년: "))
# month = int(input("월: "))
# day = int(input("일: "))
# temp = int(input("온도: "))
# weather = input("날씨: ")
# print(str % (year, month, day, temp, weather))

# 문자열 함수
str = input("문자열을 입력하세요: ")
str_len = len(str)
print(str_len)
