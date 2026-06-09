import streamlit as st
import pandas as pd
import random

st.title("TOEIC単語クイズ")

# CSV読み込み
df = pd.read_csv("words.csv")
words = df.to_dict("records")

# 初回設定
if "score" not in st.session_state:
    st.session_state.score = 0

if "count" not in st.session_state:
    st.session_state.count = 0

if "quiz" not in st.session_state:
    st.session_state.quiz = random.choice(words)

# 問題表示
st.subheader("問題")

st.write(
    f"英単語：{st.session_state.quiz['word']}"
)

answer = st.text_input("意味を入力")

# 答え合わせ
if st.button("答え合わせ"):

    st.session_state.count += 1

    if answer.strip() == st.session_state.quiz["meaning"]:

        st.success("正解！")
        st.session_state.score += 1

    else:

        st.error(
            f"不正解！正解は {st.session_state.quiz['meaning']}"
        )

    st.session_state.quiz = random.choice(words)

    st.rerun()

# 成績
if st.session_state.count > 0:

    rate = (
        st.session_state.score
        / st.session_state.count
        * 100
    )

    st.write(f"正解数: {st.session_state.score}")
    st.write(f"問題数: {st.session_state.count}")
    st.write(f"正答率: {rate:.1f}%")

    #python -m streamlit run app.py アプリ起動