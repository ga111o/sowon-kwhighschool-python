import streamlit as st

title = st.text_input("제목")
content = st.text_area("본문")

# 사이드바에 버튼 추가
if st.button("입력하기"):
    # 입력된 내용을 txt 파일로 저장
    with open(f"./folder/{title}.txt", "w") as f:
        f.write(content)
    st.sidebar.success("파일이 저장되었습니다: output.txt")
