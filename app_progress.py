import streamlit as st
import time


# プロセス中にスピナー（ループアニメーション）を表示する
with st.spinner(text='In progress'):
    time.sleep(3)
    st.success('Done')

# 進捗バーを表示して更新する
bar = st.progress(100)
for i in range(0, 100, 10):
    bar.progress(i)
    time.sleep(0.3)
bar.progress(100)
