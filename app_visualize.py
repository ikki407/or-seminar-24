import streamlit as st
import pandas as pd
import numpy as np


# 棒グラフ
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

# 棒グラフ (horizontal)
chart_data = pd.DataFrame(
    {'a': range(20),
     'b': np.random.randn(20),
     'c': np.random.randn(20)
     }
)
st.bar_chart(chart_data, x="a", y="b", color="c", horizontal=True)

# 折れ線グラフ
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

# scatterプロット
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)
