import streamlit as st

if 'count' not in st.session_state:
    st.session_state["count"] = 0

# 이거 보여줘면서 딕셔너리랑 비슷하다고 강조.
st.write(f"session state: {st.session_state}")

# init 부분에 key로 count 말고 다른 값도 넣으면서 딕셔너리처럼 관리할 수 있다고 보이기.
# 메시지랑, 역할을 이걸로 관리하면, 채팅 내역을 보관할 수 있겠죠~~


if st.button('Increment'):
    st.session_state["count"] += 1
    st.write(f"Counter incremented! New count: {st.session_state.count}")
