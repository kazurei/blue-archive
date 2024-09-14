import streamlit as st
import pandas as pd
import random

st.title("クイズアプリ")

# Excelファイルを読み込む
@st.cache_data
def load_excel(file_path):
    return pd.read_excel(file_path)

# Excelファイルのパスを指定
df = load_excel('questions.xlsx')  # Excelファイル名を指定

# クイズデータの準備
quiz_data = []
for _, row in df.iterrows():
    question = row['問題']
    correct_answer = row['正解']
    
    # サンプルの選択肢を用意（この例では固定の選択肢を使用）
    # 実際には他の選択肢も追加する必要があります
    options = [correct_answer, "選択肢A", "選択肢B", "選択肢C"]
    random.shuffle(options)  # 選択肢をシャッフル

    quiz_data.append((question, correct_answer, options))

# クイズの状態管理
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

# 現在の質問を表示
def show_question(index):
    question, correct_answer, options = quiz_data[index]
    st.write(f"問題 {index + 1}: {question}")
    selected_option = st.radio("選択肢を選んでください:", options)

    if st.button("回答"):
        check_answer(selected_option)

# ユーザーの答えを確認
def check_answer(selected_option):
    _, correct_answer, _ = quiz_data[st.session_state.question_index]
    if selected_option == correct_answer:
        st.session_state.score += 1
        st.write("正解!")
    else:
        st.write(f"不正解。正解は: {correct_answer}")

    next_question()

# 次の質問へ進む
def next_question():
    if st.session_state.question_index < len(quiz_data) - 1:
        st.session_state.question_index += 1
        st.experimental_rerun()
    else:
        st.write(f"クイズ終了! あなたのスコアは {st.session_state.score} / {len(quiz_data)}")
        if st.button("もう一度やる"):
            st.session_state.score = 0
            st.session_state.question_index = 0
            st.experimental_rerun()

# クイズのUI
if st.session_state.question_index < len(quiz_data):
    show_question(st.session_state.question_index)
else:
    st.write(f"クイズ終了! あなたのスコアは {st.session_state.score} / {len(quiz_data)}")
    if st.button("もう一度やる"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.experimental_rerun()
