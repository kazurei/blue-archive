import streamlit as st
import pandas as pd
import random

# Excelファイルの読み込み
df = pd.read_excel('blue archive.xlsx')

# クイズの問題列、正解列、誤答列の設定
questions = df.iloc[:, 0].tolist()  # 1列目：問題
correct_answers = df.iloc[:, 1].tolist()  # 2列目：正解

# 回答結果を保持するためのセッション状態を初期化
if "current_index" not in st.session_state:
    st.session_state.current_index = random.randint(0, len(questions) - 1)
if "answered" not in st.session_state:
    st.session_state.answered = False
    st.session_state.result = ""

# 現在の問題と正解を取得
current_index = st.session_state.current_index
question = questions[current_index]
correct_answer = correct_answers[current_index]

# 他の問題から誤答をランダムに選ぶ
other_answers = [answer for i, answer in enumerate(correct_answers) if i != current_index]
choices = random.sample(other_answers, 3) + [correct_answer]  # 正解と誤答を含む選択肢
random.shuffle(choices)

# Streamlitで問題を表示
st.title("ブルアカ苗字クイズ")

# ランダムで選んだ問題を表示
st.write(question)

# ボタンで選択肢を表示
for choice in choices:
    if st.button(choice):
        if not st.session_state.answered:
            if choice == correct_answer:
                st.session_state.result = "正解です！"
            else:
                st.session_state.result = f"間違いです。正解は「{correct_answer}」です。"
            st.session_state.answered = True

# 結果を表示
if st.session_state.answered:
    st.write(st.session_state.result)
    if st.button("次の問題へ"):
        st.session_state.current_index = random.randint(0, len(questions) - 1)
        st.session_state.answered = False
        st.session_state.result = ""
