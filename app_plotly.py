import streamlit as st
import numpy as np
import plotly.figure_factory as ff

# ヒストグラムのデータを追加
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# データをグループ化
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# カスタムのbin_sizeを指定してdistplotを作成
fig = ff.create_distplot(
    hist_data, group_labels, bin_size=[.1, .25, .5])

# プロットする
st.plotly_chart(fig, use_container_width=True)
