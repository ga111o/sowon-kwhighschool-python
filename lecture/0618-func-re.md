---
marp: true
theme:
paginate: true
---

### 함수란?

- 함수는 특정 작업을 수행하는 코드 블록
- 코드의 재사용성을 높이고, 코드의 구조를 더 체계적으로 만들 수 있다.
- 함수를 정의할 때는 `def` 키워드를 사용한다.

---

### 함수 정의

```python
def 함수이름(매개변수1, 매개변수2, ...):
    """코드"""
    return 반환값
```

---

### 함수 예제

```python

def add(a, b):
    """두 수를 더하는 함수"""
    return a + b

```

```python

result = add(3, 5)
print(result)  # 출력: 8

```

---

### 예제

리스트의 모든 요소를 더하는 함수

```python

def sum_list(lst):
    # 코드 작성
    return

lists = [1, 2, 3, 4, 5]
result = sum_list(lists)
print(result)  # 출력: 15

```

---

### 예제

리스트의 모든 요소를 더하는 함수

```python

def sum_list(lists):
    total = 0
    for num in lists:
        total += num
    return total

lists = [1, 2, 3, 4, 5]
result = sum_list(lists)
print(result)  # 출력: 15

```
