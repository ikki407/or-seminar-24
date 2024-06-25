import streamlit as st
import pandas as pd
import random


df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})

st.dataframe(df)  # データフレーム表記
st.table(df.iloc[0:10])  # 静的なテーブル表記
st.json({'foo': 'bar', 'fu': 'ba'})  # JSON表記
st.metric(label='Temp', value='273 K', delta='1.2 K')  # メトリック表示

# クリックしたら展開するGUIコンポーネント
with st.expander('pd.DataFrameのhelp'):
    st.help(pd.DataFrame)  # ヘルプ表示


st.divider()
st.write('データフレームをリッチに表示')
df = pd.DataFrame(
    {
        'name': ['Roadmap', 'Extras', 'Issues'],
        'url': ['https://roadmap.streamlit.app', 'https://extras.streamlit.app', 'https://issues.streamlit.app'],
        'stars': [random.randint(0, 1000) for _ in range(3)],
        'views_history': [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        'name': 'App name',
        'stars': st.column_config.NumberColumn(
            'Github Stars',
            help='Number of stars on GitHub',
            format='%d ⭐',
        ),
        'url': st.column_config.LinkColumn('App URL'),
        'views_history': st.column_config.LineChartColumn(
            'Views (past 30 days)', y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
