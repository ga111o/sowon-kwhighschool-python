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

# year = int(input("연도를 입력하세요: "))

# # 윤년 판별
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year}년 윤년 O")  # 400으로 나누어떨어지면 윤년이다.
#         else:
#             print(f"{year}년 윤년 X")  # 100으로 나누어떨어지만 400으로 나누어떨어지지 않으면 윤년이 아니다.
#     else:
#         print(f"{year}년 윤년 O")  # 4로 나누어떨어지고 100으로 나누어떨어지지 않으면 윤년이다.
# else:
#     print(f"{year}년 윤년 X")  # 4로 나누어떨어지지 않으면 윤년이 아니다.

# for i in range(1,30):
#   print(i)
#   for k in range(10,20):
#     print(i, k)

# fruits = ["사과", "바나나", "오렌지"]
# for test in fruits:
#     print(test)


# array = [1, 2, 3, 4, 10]

# for i in array:
#   print(i)

# for i in range(1,15):
#   print(i)

# for i in "ga1ahad":
#   print(i)

# for i in range(1, 4):
#     print(" " * (3 - i) + "*" * (2 * i - 1))
# for i in range(2, 0, -1):
#     print(" " * (3 - i) + "*" * (2 * i - 1))
# for i in range(20, 0, -1):
#     print(i)


# for i in range(1,6):
#     print("*"*i)



# numbers = [7, 12, 18, 21, 10, 25, 6, 24, 20, 2, 14, 5, 22, 13, 23, 8, 3, 16, 17, 19, 28, 11, 30, 9, 15, 27, 26, 29, 4, 1]

# for number in numbers:
#     if number % 2 == 0:
#         continue
#     if number >= 25:
#         break
#     print(number)


while(True):
    num = int(input("숫자 입력: "))
    is_prime = True

    if num == 0:
        break

    elif num == 1:
        print("소수 X")
        continue
    
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
    
    if is_prime == True:
        print("소수 O")
    else:
        print("소수 X")

            
