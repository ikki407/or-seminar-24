import streamlit as st
import pandas as pd
import time


# 任意の要素を置換する
element = st.empty()
element.write('プロット中')
time.sleep(3)

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})
st.line_chart(df)

time.sleep(1)
element.write('プロット完了')


# st.divider()
# # 順序を入れ替えて挿入する。
# elements = st.container()
# elements.line_chart(df)
# st.write('Hello. Out side of container.')
# elements.text_input(label='Text input')  # "Hello" より上に表示される。
