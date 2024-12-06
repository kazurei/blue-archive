import streamlit as st
import pandas as pd
import random

# Excelファイルの読み込み
df = pd.read_excel('path_to_your_excel_file.xlsx')

# 問題と正解の列を取り出す
questions = df.iloc[:, 0].tolist()  # 1列目が問題
answers = df.iloc[:, 1].tolist()  # 2列目が答え

# 誤答候補を生成するために、他の問題の答えをランダムに使う
def get_incorrect_answers(correct_answer, answers, num_choices=3):
    incorrect_answers = [answer for answer in answers if answer != correct_answer]
    return random.sample(incorrect_answers, num_choices)

# Streamlitで問題を表示
st.title("Quiz App")

# ランダムで問題を選ぶ
random_index = random.randint(0, len(questions) - 1)
question = questions[random_index]
correct_answer = answers[random_index]

# 誤答をランダムに選ぶ
incorrect_answers = get_incorrect_answers(correct_answer, answers)

# 正解と誤答を含む選択肢を作成
choices = incorrect_answers + [correct_answer]
random.shuffle(choices)

# 問題を表示
st.write(question)

# ユーザーに選択肢を表示して、答えを選ばせる
selected_answer = st.radio("選択してください", choices)

# 回答結果を表示
if selected_answer == correct_answer:
    st.success("正解です！")
else:
    st.error(f"間違いです。正解は「{correct_answer}」です。")
