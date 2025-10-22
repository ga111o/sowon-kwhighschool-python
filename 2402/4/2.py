import streamlit as st
import os

# 파일 목록 가져오기
folder = os.listdir("./folder/")

##################################################
# method1

# 사이드바에 파일 목록 표시
st.sidebar.title("파일 목록")
selected_file = st.sidebar.selectbox("파일 선택", folder)

# 선택한 파일 내용 표시
if selected_file:
    file_path = "./folder/"+selected_file
    with open(file_path, 'r') as file:
        file_content = file.read()
        st.write(file_content)

##################################################
# method2

# st.sidebar.title("파일 목록")
# for file in folder:
#     if st.sidebar.button(file):
#         file_path = "./folder/"+file
#         with open(file_path, 'r') as f:
#             file_content = f.read()
#             st.write(file_content)
