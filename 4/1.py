import streamlit as st

# 제목 설정
st.title("계산기")

# 사용자 입력 받기
number1 = st.number_input("첫 번째 숫자를 입력하세요:", value=0)
number2 = st.number_input("두 번째 숫자를 입력하세요:", value=0)

# 연산 선택
operation = st.selectbox("연산을 선택하세요:", ["더하기", "빼기", "곱하기", "나누기"])

# 계산 수행1
if operation == "더하기":
    result = number1 + number2
elif operation == "빼기":
    result = number1 - number2
elif operation == "곱하기":
    result = number1 * number2
elif operation == "나누기":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "0으로 나눌 수 없습니다."

# 결과 출력
st.write("결과:", result)
