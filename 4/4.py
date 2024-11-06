import streamlit as st

st.balloons()


st.caption("""
# 안녕하세요!
""")

color = st.color_picker("pick a color!")
st.write(color)
