import streamlit as st

st.title("英単語帳アプリ")

if "words" not in st.session_state:
    st.session_state.words = []

word = st.text_input("英単語")
meaning = st.text_input("意味")

if st.button("登録"):
    st.session_state.words.append(
        {"word": word, "meaning": meaning}
    )

st.subheader("登録単語一覧")

for w in st.session_state.words:
    st.write(f"{w['word']} : {w['meaning']}")