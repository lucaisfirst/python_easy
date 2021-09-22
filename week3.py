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

# # 문자열 길이 함수
# str = input("문자열을 입력하세요: ")
# str_len = len(str)
# print("입력받은 문자열은 %s이고, 길이는 %d입니다." % (str, str_len))

# # 문자열 count
# str = input("문자열을 입력하세요: ")
# sub_str = input("확인할 문자열을 입력하세요: ")
# count = str.count(sub_str)
# print("%s문자열에는 %s문자열이 %d개 있습니다." % (str, sub_str, count))

# # 문자열 find, index
# str = input("문자열을 입력하세요: ")
# sub_str = input("확인할 문자열을 입력하세요: ")
# print("%d" % str.find(sub_str))
# print("%d" % str.index(sub_str))

# # 구분 문자열 join 연결함수
# str = "..".join("abcd")
# print(str)
# str = " ".join(['aa', 'bb', 'cc'])
# print(str)

# # 구분 문자열 split 함수
# str = "aa bb cc".split(' ')
# print(str)

# # 대문자 소문자 변경
# str = input("문자열을 입력하시요: ")
# print("입력문자열: %s -> 대문자로 변경: %s" % (str, str.upper()))
# print("입력문자열: %s -> 소문자로 변경: %s" % (str, str.lower()))

# # rstrip, lstrip 관련해서
# print("abc  ".rstrip())
# print("  abc".lstrip())

# # replace 함수
# print("ab ab abcd abc".replace("ab", "yz"))
