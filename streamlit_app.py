import streamlit as st
import pandas as pd
import random

tab_titles = ["苗字クイズ", "固有武器"]
tab1, tab2 = st.tabs(tab_titles)

# 共通処理: セッション状態の初期化
def initialize_quiz_state(tab_name, num_questions):
    if f"current_index_{tab_name}" not in st.session_state:
        st.session_state[f"current_index_{tab_name}"] = random.randint(0, num_questions - 1)
    if f"answered_{tab_name}" not in st.session_state:
        st.session_state[f"answered_{tab_name}"] = False
        st.session_state[f"result_{tab_name}"] = ""
    if f"correct_{tab_name}" not in st.session_state:
        st.session_state[f"correct_{tab_name}"] = False
    if f"choices_{tab_name}" not in st.session_state:
        st.session_state[f"choices_{tab_name}"] = []

with tab1:
    st.header("苗字クイズ")
    df = pd.read_excel('blue archive.xlsx')

    questions = df.iloc[:, 0].tolist()  # 1列目：問題
    correct_answers = df.iloc[:, 1].tolist()  # 2列目：正解

    # セッション状態の初期化（苗字クイズ用）
    initialize_quiz_state("tab1", len(questions))

    # 現在の問題と正解を取得
    current_index = st.session_state["current_index_tab1"]
    question = questions[current_index]
    correct_answer = correct_answers[current_index]

    # 選択肢を保持または作成
    if not st.session_state["choices_tab1"]:
        other_answers = [answer for i, answer in enumerate(correct_answers) if i != current_index]
        st.session_state["choices_tab1"] = random.sample(other_answers, 3) + [correct_answer]
        random.shuffle(st.session_state["choices_tab1"])

    # 問題が正しく取得できているか確認
    if not question or question is None:
        st.error("問題が正しく取得できませんでした。")
    else:
        # Streamlitで問題を表示
        st.title("ブルアカ苗字クイズ")
        st.write("このキャラクターの苗字は？：" + question)

        # ボタンで選択肢を表示
        for choice in st.session_state["choices_tab1"]:
            if isinstance(choice, str) and choice.strip():  # choiceが文字列であり、空でないことを確認
                if st.button(choice):
                    if not st.session_state["answered_tab1"]:
                        if choice == correct_answer:
                            st.session_state["result_tab1"] = "正解です！"
                            st.session_state["correct_tab1"] = True
                        else:
                            st.session_state["result_tab1"] = f"間違いです。正解は「{correct_answer}」です。"
                            st.session_state["correct_tab1"] = False
                        st.session_state["answered_tab1"] = True

    # 結果を表示
    if st.session_state["answered_tab1"]:
        st.write(st.session_state["result_tab1"])
        if st.button("次の問題へ"):
            st.session_state["current_index_tab1"] = random.randint(0, len(questions) - 1)
            st.session_state["answered_tab1"] = False
            st.session_state["result_tab1"] = ""
            st.session_state["correct_tab1"] = False
            st.session_state["choices_tab1"] = []

with tab2:
    st.header("固有武器")
    df = pd.read_excel('blue archive.xlsx')

    questions = df.iloc[:, 2].astype(str).tolist()  # 3列目：問題を文字列に変換
    correct_answers = df.iloc[:, 3].astype(str).tolist()  # 4列目：答えを文字列に変換

    # データが空でないか確認
    if not questions or not correct_answers:
        st.error("問題または正解データが空です。Excelファイルを確認してください。")
    else:
        # セッション状態の初期化（固有武器用）
        initialize_quiz_state("tab2", len(questions))

        # 現在の問題と正解を取得
        current_index = st.session_state["current_index_tab2"]
        
        # current_index が有効か確認
        if current_index < 0 or current_index >= len(questions):
            st.error(f"無効なインデックスです: {current_index}. インデックスが範囲外です。")
        else:
            question = questions[current_index]
            correct_answer = correct_answers[current_index]

            # 選択肢を保持または作成
            if not st.session_state["choices_tab2"]:
                other_answers = [answer for i, answer in enumerate(correct_answers) if i != current_index]
                st.session_state["choices_tab2"] = random.sample(other_answers, 3) + [correct_answer]
                random.shuffle(st.session_state["choices_tab2"])

            # 問題が正しく取得できているか確認
            if not isinstance(question, str) or not question.strip():  # 文字列かつ空でないかを確認
                st.error("問題が正しく取得できませんでした。")
            else:
                # 問題が取得できている場合にのみ表示
                st.title("ブルアカ固有武器クイズ")
                st.write("このキャラクターの固有武器は？：" + question)

                # ボタンで選択肢を表示
                for choice in st.session_state["choices_tab2"]:
                    if isinstance(choice, str) and choice.strip():  # choiceが文字列であり、空でないことを確認
                        if st.button(choice):
                            if not st.session_state["answered_tab2"]:
                                if choice == correct_answer:
                                    st.session_state["result_tab2"] = "正解です！"
                                    st.session_state["correct_tab2"] = True
                                else:
                                    st.session_state["result_tab2"] = f"間違いです。正解は「{correct_answer}」です。"
                                    st.session_state["correct_tab2"] = False
                                st.session_state["answered_tab2"] = True

        # 結果を表示
        if st.session_state["answered_tab2"]:
            st.write(st.session_state["result_tab2"])
            if st.button("次の問題へ"):
                st.session_state["current_index_tab2"] = random.randint(0, len(questions) - 1)
                st.session_state["answered_tab2"] = False
                st.session_state["result_tab2"] = ""
                st.session_state["correct_tab2"] = False
                st.session_state["choices_tab2"] = []

    