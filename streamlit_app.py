import streamlit as st
import pandas as pd
import random
tab_titles=["苗字クイズ","固有武器"]
tab1,tab2=st.tabs(tab_titles)
with tab1:
    st.header("苗字クイズ")
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
    if "correct" not in st.session_state:
      st.session_state.correct = False
    if "choices" not in st.session_state:
      st.session_state.choices = []
  
  # 現在の問題と正解を取得
    current_index = st.session_state.current_index
    question = questions[current_index]
    correct_answer = correct_answers[current_index]
  
  # 選択肢を保持または作成
    if not st.session_state.choices:
      other_answers = [answer for i, answer in enumerate(correct_answers) if i != current_index]
      st.session_state.choices = random.sample(other_answers, 3) + [correct_answer]  # 正解と誤答を含む選択肢
      random.shuffle(st.session_state.choices)
  
  # Streamlitで問題を表示
    st.title("ブルアカ苗字クイズ")
  
  # ランダムで選んだ問題を表示
    st.write("このキャラクターの苗字は？："+ question)
  
  # ボタンで選択肢を表示
    for choice in st.session_state.choices:
      if st.button(choice):
          if not st.session_state.answered:
              if choice == correct_answer:
                  st.session_state.result = "正解です！"
                  st.session_state.correct = True
              else:
                  st.session_state.result = f"間違いです。正解は「{correct_answer}」です。"
                  st.session_state.correct = False
              st.session_state.answered = True
  
  # 結果を表示
    if st.session_state.answered:
      st.write(st.session_state.result)
      if st.button("次の問題へ"):
          st.session_state.current_index = random.randint(0, len(questions) - 1)
          st.session_state.answered = False
          st.session_state.result = ""
          st.session_state.correct = False
          st.session_state.choices = []

with tab2:
    st.header("固有武器")
    df = pd.read_excel('blue archive.xlsx')
    questions = df.iloc[:, 3].tolist()  # 1列目：問題
    correct_answers = df.iloc[:, 4].tolist()  # 2列目：正解
  
  # 回答結果を保持するためのセッション状態を初期化
    if "current_index" not in st.session_state:
      st.session_state.current_index = random.randint(0, len(questions) - 1)
    if "answered" not in st.session_state:
      st.session_state.answered = False
      st.session_state.result = ""
    if "correct" not in st.session_state:
      st.session_state.correct = False
    if "choices" not in st.session_state:
      st.session_state.choices = []
  
  # 現在の問題と正解を取得
    current_index = st.session_state.current_index
    question = questions[current_index]
    correct_answer = correct_answers[current_index]
  
  # 選択肢を保持または作成
    if not st.session_state.choices:
      other_answers = [answer for i, answer in enumerate(correct_answers) if i != current_index]
      st.session_state.choices = random.sample(other_answers, 3) + [correct_answer]  # 正解と誤答を含む選択肢
      random.shuffle(st.session_state.choices)
  
  # Streamlitで問題を表示
    st.title("ブルアカ固有武器クイズ")
  
  # ランダムで選んだ問題を表示
    st.write("このキャラクターの固有武器は？："+ question)
  
  # ボタンで選択肢を表示
    for choice in st.session_state.choices:
      if st.button(choice):
          if not st.session_state.answered:
              if choice == correct_answer:
                  st.session_state.result = "正解です！"
                  st.session_state.correct = True
              else:
                  st.session_state.result = f"間違いです。正解は「{correct_answer}」です。"
                  st.session_state.correct = False
              st.session_state.answered = True
  
  # 結果を表示
    if st.session_state.answered:
      st.write(st.session_state.result)
      if st.button("次の問題へ"):
          st.session_state.current_index = random.randint(0, len(questions) - 1)
          st.session_state.answered = False
          st.session_state.result = ""
          st.session_state.correct = False
          st.session_state.choices = []