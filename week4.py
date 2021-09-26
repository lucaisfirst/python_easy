print("시험에 응시하시겠습니까? 응시:1 미응시: 1이 아닌 수")
flag = int(input())

if flag == 1:
    print("시험에 응시하였습니다.")
    print("점수를 입력해주세요.")
    score = int(input())

    if score > 100 or score < 0:
        print("점수를 잘못 입력하셨습니다. 점수의 크기는 0보다 크거나 작고, 100보다 작거나 같습니다.")
    elif score >= 90:
        print("점수는 A")
    elif score >= 80:
        print("점수는 B입니다.")
    elif score >= 70:
        print("점수가 C입니다.")
    elif score >= 60:
        print("점수가 C입니다.")
    else:
        print("점수가 F입니다.")
else:
    print("시험에 결시하였습니다.")
