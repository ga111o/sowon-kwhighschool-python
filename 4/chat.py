import streamlit as st


def get_bot_response(user_input):

    if "안녕" in user_input:
        return "안녕하세요! 무엇을 도와드릴까요?"
    elif "날씨" in user_input:
        return "오늘의 날씨는 맑습니다!"
    elif "고마워" in user_input:
        return "천만에요!"
    else:
        return "죄송하지만, 이해하지 못했습니다."


if 'messages' not in st.session_state:
    st.session_state.messages = []


user_input = st.text_input("메시지를 입력하세요:")


if st.button("전송"):

    st.session_state.messages.append({"role": "user", "content": user_input})

    bot_response = get_bot_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_response})


for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**사용자:** {message['content']}")
    else:
        st.write(f"**챗봇:** {message['content']}")
