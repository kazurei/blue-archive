import streamlit as st
import pandas as pd
import random

# Excelファイルの読み込み
df = pd.read_excel('path_to_your_excel_file.xlsx')

# クイズの問題列、正解列、誤答列の設定
questions = df.iloc[:, 0].tolist()  # 1列目：問題
correct_answers = df.iloc[:, 1].tolist()  # 2列目：正解
incorrect_answers = df.iloc[:, 1].tolist()  # 正解を誤答候補として使用

# 1問をランダムに選ぶ
random_index = random.randint(0, len(questions) - 1)
question = questions[random_index]
correct_answer = correct_answers[random_index]

# 他の問題から誤答をランダムに選ぶ
other_answers = [answer for i, answer in enumerate(correct_answers) if i != random_index]
choices = random.sample(other_answers, 3) + [correct_answer]  # 正解と誤答を含む選択肢
random.shuffle(choices)

# Streamlitで問題を表示
st.title("クイズアプリ")

# ランダムで選んだ問題を表示
st.write(question)

# ユーザーに選択肢を表示して、答えを選ばせる
selected_answer = st.radio("選択してください", choices)

# 回答結果を表示
if selected_answer == correct_answer:
    st.success("正解です！")
else:
    st.error(f"間違いです。正解は「{correct_answer}」です。")
