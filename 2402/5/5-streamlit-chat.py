from langchain.prompts import ChatPromptTemplate
from langchain.callbacks.base import BaseCallbackHandler
import streamlit as st
import google.generativeai as genai

st.set_page_config(  # 처음 할 땐 이거 없이
    page_title="Document",
    page_icon="📃",
)


def save_message(message, role):
    chat = {"message": message, "role": role}
    st.session_state["messages"].append(chat)


def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        save_message(message, role)


def paint_history():
    for message in st.session_state["messages"]:
        send_message(
            message["message"],
            message["role"],
            save=False,
        )


st.title("ga111o!")
st.session_state["messages"] = []

send_message("I'm ready! Ask away!", "ai", save=False)
paint_history()
message = st.chat_input("Ask anything about your file...")
if message:
    send_message(message, "human")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(message)
    send_message(response.text, "ai")


else:
    st.session_state["messages"] = []
