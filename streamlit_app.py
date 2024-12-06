import streamlit as st
import pandas as pd
import random

# ローカルファイルからExcelファイルを読み込む関数
def load_questions_from_local(file_path):
    # pandasのread_excel関数を使ってローカルファイルを読み込む
    df = pd.read_excel(file_path)
    return df

# アプリケーションのUI部分
def app():
    st.title("問題出題アプリ")

    # ローカルのExcelファイルのパス
    file_path = 'blue archive.xlsx'  # ローカルのファイルパスを指定

    # Excelファイルを読み込む
    try:
        questions_df = load_questions_from_local(file_path)
        st.write("問題データが正常に読み込まれました。")

        # DataFrameの表示（デバッグ用）
        st.write(questions_df)

        # 問題が読み込まれた場合
        if not questions_df.empty:
            # 問題をランダムにシャッフル
            questions = questions_df['問題'].tolist()
            answers = questions_df['答え'].tolist()

            # 正解以外の誤答を他の問題の答えからランダムに選ぶ
            incorrect_answers_pool = [ans for ans in answers]

            # 問題と選択肢をランダムに出題
            for idx, question in enumerate(random.sample(questions, len(questions))):  # 問題をランダムに出題
                correct_answer = answers[questions.index(question)]
                
                # ここでは他の問題の答えからランダムに誤答を選ぶ
                incorrect_answers = random.sample([ans for ans in incorrect_answers_pool if ans != correct_answer], 3)

                # 正解を含めて選択肢を作成
                options = [correct_answer] + incorrect_answers
                random.shuffle(options)  # 選択肢をランダムに並べ替え

                # 問題を表示
                st.write(f"問題 {idx + 1}: {question}")
                answer = st.radio("選択肢", options, key=f"question_{idx}")

                # 正誤判定
                if st.button('回答', key=f'button_{idx}'):
                    if answer == correct_answer:
                        st.success("正解！")
                    else:
                        st.error("不正解。")
        else:
            st.warning("問題がありません。Excelファイルを確認してください。")
    except Exception as e:
        st.error(f"Excelファイルの読み込みに失敗しました: {e}")

if __name__ == "__main__":
    app()
