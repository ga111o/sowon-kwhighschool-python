import streamlit as st

# 이거 만드는데 코드 30줄이면 충분하다고 강조,
# 실제로 보여주면서
# 스트림릿은 쩌는 툴이다 강조

# 페이지 제목
st.title("포트폴리오")

# 사이드바 네비게이션
st.sidebar.header("네비게이션")
page = st.sidebar.selectbox("페이지 선택", ["소개", "프로젝트", "기술 스택", "연락처"])

# 페이지에 따라 내용 표시
if page == "소개":
    st.header("소개")
    st.image("./icon.png", width=100)  # 이미지 크기 조절
    st.write("안녕하세요! 저는 자연어처리를 공부하는 개발자입니다!")
    st.toast("반가워요!")


elif page == "프로젝트":
    st.header("프로젝트")
    projects = {
        "프로젝트 1": {
            "description": "데이터 시각화 웹 애플리케이션",
            "code": "print('hello world')",
            "lang": "python",
            "link": "https://github.com/ga111o/project1"
        },
        "프로젝트 2": {
            "description": "머신러닝 모델 개발",
            "code": "console.log('hello world')",
            "lang": "javascript",
            "link": "https://github.com/ga111o/project2"
        },
        "프로젝트 3": {
            "description": "자연어 처리 프로젝트",
            "code": "안녕하세요",
            "lang": "text",
            "link": "https://github.com/ga111o/project3"
        }
    }

    for project, info in projects.items():
        st.subheader(project)
        st.write(info["description"])
        st.code(info["code"], language=info["lang"])
        st.markdown(f"[GitHub 링크]({info['link']})")

elif page == "기술 스택":
    st.header("기술 스택")
    technologies = ["Python", "Streamlit", "Pandas",
                    "NumPy", "Matplotlib", "Scikit-learn"]
    st.write(", ".join(technologies))

elif page == "연락처":
    st.header("연락처")
    st.write("E-mail: email@example.com")
    st.write("LinkedIn: [링크](https://www.linkedin.com)")
