# 각기 다른 변수 선언
a = 1
b = 3.14
c = "Python"

# 변수에 저장된 값 출력
print(a)
print(b)
print(c)

a = 3.14
print(a)

a = "Python"
print(a)

# 변수의 데이터 타입 출력 및 확인
a = 1
b = 3.14
c = 2 + 3j
print(type(a))
print(type(b))
print(type(c))

# 변수의 데이터 타입 casting
print(float(2))
print(str(2))

a = 3
print(type(a))

# 사각형, 삼각형의 넓이
wid = 3.3
len = 7.2

area1 = wid*len
area2 = (wid*len)/2

print("사각형의 넓이:", area1)
print("삼각형의 넓이", area2)
print("사각형의 넓이: %f" % area1)
