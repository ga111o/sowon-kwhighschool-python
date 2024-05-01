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
