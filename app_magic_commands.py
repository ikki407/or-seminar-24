import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# タイトルとテキストをアプリに直接表示
'''
# This is the document title

This is **some** _markdown_.
'''

# データフレームを表示
df = pd.DataFrame({'col1': [1, 2, 3]})
df

# 文字列'x'と変数xの値を表示
x = 10
'x = ', x

# matplotlibの図を表示
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig
