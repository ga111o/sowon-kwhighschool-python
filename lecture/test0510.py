age = 16

# if age < 20:
#   print("학생")

# if 1:
#   print("1")

# if 0:
#   print("1")

# if True:
#   print("True")

# if age<10:
#   print("어린이")

# elif age>=10 and age<20:
#   print("학생")

# elif age >= 20:
#   print("성인")

# if 10 - 5 - 10:
#   print("what")

# num = 13

# if (num % 2):
#   print("홀수")
# else:
#   print("짝수")

year = int(input("연도를 입력하세요: "))

# 윤년 판별
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}년 윤년 O")  # 400으로 나누어떨어지면 윤년이다.
        else:
            print(f"{year}년 윤년 X")  # 100으로 나누어떨어지지만 400으로 나누어떨어지지 않으면 윤년이 아니다.
    else:
        print(f"{year}년 윤년 O")  # 4로 나누어떨어지고 100으로 나누어떨어지지 않으면 윤년이다.
else:
    print(f"{year}년 윤년 X")  # 4로 나누어떨어지지 않으면 윤년이 아니다.
