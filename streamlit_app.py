import streamlit as st
import pandas as pd
import random

tab_titles = ["苗字クイズ", "固有武器","所属部活"]
tab1, tab2 ,tab3= st.tabs(tab_titles)

with tab1:
    # Excelファイルの読み込み
    df = pd.read_excel('blue archive.xlsx')

    # クイズの問題列、正解列の設定
    questions = df.iloc[:, 0].tolist()  # 1列目：問題
    correct_answers = df.iloc[:, 1].tolist()  # 2列目：正解

    # 回答結果を保持するためのセッション状態を初期化（苗字クイズ用）
    if "current_index_m" not in st.session_state:
        st.session_state.current_index_m = random.randint(0, len(questions) - 1)
    if "answered_m" not in st.session_state:
        st.session_state.answered_m = False
        st.session_state.result_m = ""
    if "correct_m" not in st.session_state:
        st.session_state.correct_m = False
    if "choices_m" not in st.session_state:
        st.session_state.choices_m = []

    # 現在の問題と正解を取得（苗字クイズ用）
    current_index_m = st.session_state.current_index_m
    question_m = questions[current_index_m]
    correct_answer_m = correct_answers[current_index_m]

    # 選択肢を保持または作成（苗字クイズ用）
    if not st.session_state.choices_m:
        other_answers_m = [answer for i, answer in enumerate(correct_answers) if i != current_index_m]
        st.session_state.choices_m = random.sample(other_answers_m, 3) + [correct_answer_m]  # 正解と誤答を含む選択肢
        random.shuffle(st.session_state.choices_m)

    # Streamlitで問題を表示（苗字クイズ用）
    st.title("ブルアカ苗字クイズ")

    # ランダムで選んだ問題を表示（苗字クイズ用）
    st.write("このキャラクターの苗字は？：" + question_m)

    # ボタンで選択肢を表示（苗字クイズ用）
    for choice in st.session_state.choices_m:
        if st.button(choice, key=f"button_m_{choice}"):  # 一意のkeyを指定
            if not st.session_state.answered_m:
                if choice == correct_answer_m:
                    st.session_state.result_m = "正解です！"
                    st.session_state.correct_m = True
                else:
                    st.session_state.result_m = f"間違いです。正解は「{correct_answer_m}」です。"
                    st.session_state.correct_m = False
                st.session_state.answered_m = True

    # 結果を表示（苗字クイズ用）
    if st.session_state.answered_m:
        st.write(st.session_state.result_m)
        if st.button("次の問題へ"):
            st.session_state.current_index_m = random.randint(0, len(questions) - 1)
            st.session_state.answered_m = False
            st.session_state.result_m = ""
            st.session_state.correct_m = False
            st.session_state.choices_m = []

with tab2:
    # Excelファイルの読み込み
    df = pd.read_excel('blue archive.xlsx')

    # 3列目（問題列）のNaNを除外
    df_cleaned = df.dropna(subset=[df.columns[2]])

    # 固有武器の問題列と正解列の設定（NaN除外後）
    questions_w = df_cleaned.iloc[:, 2].tolist()  # 3列目：問題
    correct_answers_w = df_cleaned.iloc[:, 3].tolist()  # 4列目：正解

    # 回答結果を保持するためのセッション状態を初期化（固有武器クイズ用）
    if "current_index_w" not in st.session_state:
        st.session_state.current_index_w = random.randint(0, len(questions_w) - 1)
    if "answered_w" not in st.session_state:
        st.session_state.answered_w = False
        st.session_state.result_w = ""
    if "correct_w" not in st.session_state:
        st.session_state.correct_w = False
    if "choices_w" not in st.session_state:
        st.session_state.choices_w = []

    # 現在の問題と正解を取得（固有武器クイズ用）
    current_index_w = st.session_state.current_index_w
    question_w = questions_w[current_index_w]
    correct_answer_w = correct_answers_w[current_index_w]

    # 選択肢を保持または作成（固有武器クイズ用）
    if not st.session_state.choices_w:
        other_answers_w = [answer for i, answer in enumerate(correct_answers_w) if i != current_index_w]
        st.session_state.choices_w = random.sample(other_answers_w, 3) + [correct_answer_w]  # 正解と誤答を含む選択肢
        random.shuffle(st.session_state.choices_w)

    # Streamlitで問題を表示（固有武器クイズ用）
    st.title("ブルアカ固有武器クイズ")

    # ランダムで選んだ問題を表示（固有武器クイズ用）
    st.write("このキャラクターの固有武器は？：" + question_w)

    # ボタンで選択肢を表示（固有武器クイズ用）
    for choice in st.session_state.choices_w:
        if st.button(choice, key=f"button_w_{choice}"):  # 一意のkeyを指定
            if not st.session_state.answered_w:
                if choice == correct_answer_w:
                    st.session_state.result_w = "正解です！"
                    st.session_state.correct_w = True
                else:
                    st.session_state.result_w = f"間違いです。正解は「{correct_answer_w}」です。"
                    st.session_state.correct_w = False
                st.session_state.answered_w = True

    # 結果を表示（固有武器クイズ用）
    if st.session_state.answered_w:
        st.write(st.session_state.result_w)
        if st.button("次の問題へ"):
            st.session_state.current_index_w = random.randint(0, len(questions_w) - 1)
            st.session_state.answered_w = False
            st.session_state.result_w = ""
            st.session_state.correct_w = False
            st.session_state.choices_w = []
##with tab3:
##     #Excelファイルの読み込み
##    df = pd.read_excel('blue archive.xlsx')
##    # 1列目（問題列）のNaNを除外
##    df_cleaned = df.dropna(subset=[df.columns[0]])
##
##    # 固有武器の問題列と正解列の設定（NaN除外後）
##    questions_a = df_cleaned.iloc[:, 0].tolist()  # 1列目：問題
##    correct_answers_a = df_cleaned.iloc[:, 5].tolist()  # 6列目：正解
##
##    # 回答結果を保持するためのセッション状態を初期化（固有武器クイズ用）
##    if "current_index_a" not in st.session_state:
##        st.session_state.current_index_a = random.randint(0, len(questions_a) - 1)
##    if "answered_a" not in st.session_state:
##        st.session_state.answered_a = False
##        st.session_state.result_a = ""
##    if "correct_a" not in st.session_state:
##        st.session_state.correct_a = False
##    if "choices_a" not in st.session_state:
##        st.session_state.choices_a = []
##
##    # 現在の問題と正解を取得（固有武器クイズ用）
##    current_index_a = st.session_state.current_index_a
##    question_a = questions_a[current_index_a]
##    correct_answer_a = correct_answers_a[current_index_a]
##
##    # 選択肢を保持または作成（固有武器クイズ用）
##    if not st.session_state.choices_a:
##        other_answers_a = [answer for i, answer in enumerate(correct_answers_a) if i != current_index_a]
##        st.session_state.choices_a = random.sample(other_answers_a, 5) + [correct_answer_a]  # 正解と誤答を含む選択肢
##        random.shuffle(st.session_state.choices_a)
##
##    # Streamlitで問題を表示（固有武器クイズ用）
##    st.title("ブルアカ固有武器クイズ")
##
##    # ランダムで選んだ問題を表示（固有武器クイズ用）
##    st.write("このキャラクターの固有武器は？：" + question_a)
##
##    # ボタンで選択肢を表示（固有武器クイズ用）
##    for choice in st.session_state.choices_a:
##        if st.button(choice, key=f"button_a_{choice}"):  # 一意のkeyを指定
##            if not st.session_state.answered_a:
##                if choice == correct_answer_a:
##                    st.session_state.result_a = "正解です！"
##                    st.session_state.correct_a = True
##                else:
##                    st.session_state.result_a = f"間違いです。正解は「{correct_answer_a}」です。"
##                    st.session_state.correct_a = False
##                st.session_state.answered_a = True
##
##    # 結果を表示（固有武器クイズ用）
##    if st.session_state.answered_a:
##        st.write(st.session_state.result_a)
##        if st.button("次の問題へ"):
##            st.session_state.current_index_a = random.randint(0, len(questions_a) - 1)
##            st.session_state.answered_a = False
##            st.session_state.result_a = ""
##            st.session_state.correct_a = False
##            st.session_state.choices_a = []