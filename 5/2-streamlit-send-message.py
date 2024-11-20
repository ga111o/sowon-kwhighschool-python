import streamlit as st


st.chat_message("human")
st.markdown("human message")

# 이렇게 스트림릿에서는 메시지를 위한 폼을 줌.
# 만약 chat message 안에 human message를 넣고 싶으면, with를 써야함.

with st.chat_message("human"):
    st.markdown("human message")

# ===============================================================


# 함수화 시키면 이렇게 됨.

def send_message(message, role):
    with st.chat_message(role):
        st.markdown(message)


send_message("human message", "human")
send_message("ai message", "ai")
send_message("user message", "user")
send_message("assistant message", "assistant")


# ===============================================================

# 입력을 하고 싶으면 아래처럼. chat input을 통해 message에 입력을 받고, 만약 입력이 존재한다면, 해당 입력을 보여주는 방식.

message = st.chat_input("chat!")
if message:
    send_message(message, "human")
    send_message("gpt의 답변", "ai")
