import streamlit as st

# 제목 설정
st.title("line_chart")

# x 값 생성
x = [i for i in range(-10, 10)]

# y 값 계산
y = []  # y 값을 저장할 리스트
for i in x:
    y.append(2 * i**3 - i**2 + 3 * i)

# 차트 그리기
st.line_chart({'x': x, 'y': y})
