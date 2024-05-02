---
marp: true
theme: gaia
---

### 파이썬 프로그래밍

# 조건문과 반복문

<img src="https://raw.githubusercontent.com/ga111o/sowon-kwhighschool-python/main/lecture/src/kwu-logo.png" style="width: 250px; position:absolute; bottom: 5%; right:5%">

---

### 조건문이란?

특정한 조건을 만족할 때 코드를 실행시키는 명령어.

주로 `if`, `elif`, `else`가 사용됨.

- if: 주어진 조건에 대해 참일 때 코드 실행
- elif: 이전 조건이 거짓일 때, 현재 조건을 체크 후, 참이라면 코드 실행
- else: 모든 이전 조건이 거짓일 때 코드 실행

---

### if 문

<div style="float:left; width: 40%; margin-right:30px">

```python
age = 18

if age < 20:
  print("학생입니다")
  print(age, "살 입니다.")

if -1:
  print("true")
  if 3:
    print("true")

if True:
  print("true")
```

</div>

조건<small>(age가 20 미만인가?)</small>에 대해 참이기에 print("") 코드 실행.

들여쓰기가 된 **코드 블록 전체**를 순서대로 실행.

**연산자**, **연산**의 결과가 참일 경우, 명시적으로 **True**를 적을 경우에도 실행.

if의 코드 블록 안에 if문을 넣을 수 있다.

---

### elif 문

<div style="float:left; width: 40%; margin-right:30px">

```python
age = 16

# 조건1
if age<10:
  print("어린이")

# 조건2
elif age>=10 and age<20:
  print("학생")
  if True:
    print("true")

# 조건3
elif age >= 20:
  print("성인")
```

</div>

조건1이 거짓이기에 조건2를 확인한다.

조건2가 참이기에 조건3은 확인하지 않는다.

기준이 되는 if문과 같은 라인에 있어야 한다.

elif의 코드 블록 안에 if문이 들어갈 수 있다.

---

### else 문

<div style="float:left; width: 40%; margin-right:30px">

```python
age = 30

# 조건1
if age<10:
  print("어린이")

# 조건2
elif age>=10 and age<20:
  print("학생")

else:
  print("성인")
  if True:
    print("true")
```

</div>

모든 조건이 거짓일 때 실행된다.

else도 elif처럼 기준이 되는 if문과 같은 라인에 있어야 한다.

else의 코드 블록 안에 if문이 들어갈 수 있다.

---

### 예제

<div style="float:right; width: 40%; margin-left:30px">

```python

num = 13

# 2로 나눈 나머지가 1 -> 홀수
if (num % 2) == 1:
  print("홀수")

# 2로 나눈 나머지가 0 -> 짝수
elif (num %; 2) == 0:
  print("짝수")

else:
  print("정수를 입력해주세요.")

```

</div>

**짝수 홀수 판별기**

2로 나눈 나머지가 1이라면 홀수
2로 나눈 나머지가 0이라면 짝수

연산 순서가 명확하지 않을 때는 괄호로 묶어서 순서를 명확하게 하는 것이 좋다.

---

### 예제

<div style="float:right; width: 40%; margin-left:30px">

```python

num = 13

if (num % 2):
  print("홀수")
else:
  print("짝수")


```

</div>

**짝수 홀수 판별기**

모든 자연수는 2로 나누면
나머지는 0 or 1이다.

---

### 예제

**윤년 판별기**

윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의
배수일 때이다.

윤년 규칙을 수학적으로 표현한다면
(n % 4 == 0) and ((n mod 100 != 0) or (n mod 400 == 0))

---

### 예제

<div style="float:right; width: 70%; margin-left:30px">

```python

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            # 400으로 나누어떨어지면 윤년이다.
            print(f"{year}년 윤년 O")
        else:
            # 100으로 나누어떨어지지만
            # 400으로 나누어떨어지지 않으면 윤년이 아니다.
            print(f"{year}년 윤년 X")
    else:
        # 4로 나누어떨어지고
        # 100으로 나누어떨어지지 않으면 윤년이다.
        print(f"{year}년 윤년 O")
else:
    # 4로 나누어떨어지지 않으면 윤년이 아니다.
    print(f"{year}년 윤년 X")

```

</div>

**윤년 판별기**

---

### 예제

<div style="float:right; width: 70%; margin-left:30px">

```python

year = int(input("연도를 입력하세요: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year}년 윤년 O")
else:
    print(f"{year}년 윤년 X")

```

</div>

**윤년 판별기**

연산의 결과가 True이면 코드 블록을 실행하는 것이기에

이렇게 최적화 가능

---
