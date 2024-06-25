import streamlit as st
import pandas as pd
import time


df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [100, 200, 300, 400]
})

df2 = pd.DataFrame([[1, 20, 300]], columns=(['A', 'B', 'C']))

# データフレームに行を追加する
element = st.dataframe(df1)
time.sleep(3)
element.add_rows(df2)

# チャートに行（データ）を追加する
element = st.line_chart(df1)
time.sleep(3)
element.add_rows(df2)
