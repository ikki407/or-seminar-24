import streamlit as st
import pandas as pd


hit = st.button('Hit me')  # ボタン（押すとTrueになる）
if hit:
    st.write('I was hit')
else:
    st.write('I was not hit')

hit_help = st.button('Help', help='This is help button!')  # ボタン（押すとTrueになる）
if hit_help:
    st.write('May I help you?')

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})
df_edit = st.data_editor(df)  # データフレームを編集
st.write('↓編集後のデータフレーム')
st.write(df_edit)  # 編集したデータベースを使いまわせる

st.checkbox('Check me out')  # チェックボックス
st.radio('Pick one:', ['nose', 'ear'])  # ラジオボタン
st.toggle('Toggle me')  # トグルボタン
st.selectbox('Select', [1, 2, 3])  # セレクトボックス
st.multiselect('Multiselect', [1, 2, 3])  # マルチセレクトボックス
st.slider('Slide me', min_value=0, max_value=10)  # スライダー
start_color, end_color = st.select_slider('Slide to select', options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'], value=['red', 'blue'])  # セレクトスライダー
st.text_input('Enter some text')  # テキスト入力
st.number_input('Enter a number')  # 数値入力
st.text_area('Area for textual entry')  # テキストエリア
st.date_input('Date input')  # 日付入力
st.time_input('Time entry')  # 時間入力
data = st.file_uploader('File uploader')  # ファイルアップローダー


# データフレームをCSVファイルに変換する（ダウンロード用）
def convert_df(df):
    return df.to_csv().encode("utf-8")


st.download_button('Download df', convert_df(df), file_name="df.csv", mime="text/csv")  # ダウンロードボタン

st.camera_input('はい、チーズ')  # カメラ入力
st.color_picker('Pick a color')  # カラーピッカー

# ウィジェットのインタラクティビティを無効化
hit = st.button('Hit me', key='enable_slider_button')
a = st.slider('Pick a number', 0, 100, disabled=not hit)
st.write('value = ', a)
