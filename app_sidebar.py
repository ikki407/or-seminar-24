import streamlit as st


# オブジェクト属性を使用してサイドバーのタイトルを設定する
st.sidebar.title('サイドバー')
add_selectbox = st.sidebar.selectbox(
    'アルゴリズム',
    ('単体法', '内点法')
)

# "with"表記を使用して、サイドバーにスライダーとボタンを追加する
with st.sidebar:
    # パラメータをスライダーで選択する
    param = st.slider('パラメータ', min_value=0, max_value=10)

    # 配送オプションボタンの実装を表示しながら、選択肢を追加する
    with st.echo():
        with st.sidebar:
            add_radio = st.radio(
                '配送オプション',
                ("Standard (5-15 days)", "Express (2-5 days)")
            )

st.write('こっちはメインのページです')
