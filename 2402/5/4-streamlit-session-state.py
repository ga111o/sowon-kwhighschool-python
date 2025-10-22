import streamlit as st


def send_message(message, role):
    with st.chat_message(role):
        st.markdown(message)


def save_message(message, role):
    chat = {"message": message, "role": role}
    st.session_state["chat"].append(chat)


def paint_history():
    for message in st.session_state["chat"]:
        send_message(
            message["message"],
            message["role"],
            save=False,
        )


# 물론 저 함수를 실행시키기 이전에 아래처럼 초기화 해주는 게 필요하다고 말하기
if "chat" not in st.session_state:
    st.session_state["chat"] = []
