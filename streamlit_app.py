import streamlit as st
st.title("")
def load_questions_from_url(url):
    # pandasのread_excel関数を使ってURLからExcelファイルを読み込む
    df = pd.read_excel(url)
    return df

# アプリケーションのUI部分
def app():
    st.title("問題出題アプリ")

    # GitHubにアップロードされたExcelファイルのURL（生のURL）
    # GitHubリポジトリのrawファイルのURLを指定してください
    file_url = 'https://github.com/your_username/your_repository/raw/main/questions.xlsx'

    # Excelファイルを読み込む
    try:
        questions_df = load_questions_from_url(file_url)
        st.write("問題データが正常に読み込まれました。")

        # DataFrameの表示（デバッグ用）
        st.write(questions_df)

        # 問題が読み込まれた場合
        if not questions_df.empty:
            # 各問題のタイトルと選択肢を出題
            for idx, row in questions_df.iterrows():
                question = row['問題']
                options = [row['選択肢1'], row['選択肢2'], row['選択肢3'], row['選択肢4']]
                correct_answer = row['正解']

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