import streamlit as st


col1, col2 = st.columns(2)

# 幅が異なる3つの列を作成
# col1, col2, col3 = st.columns([3, 1, 1])  # col1が幅広い

# 'with'構文を使用する場合
with col1:
    st.write('Column 1')
    st.markdown('#### Column 1 markdown')
    st.write('This is column 1')

with col2:
    st.write('Column 2')
    st.write('This is column 2')


# 3つの列を作成し、それぞれに画像を表示
st.markdown('---')  # st.devide()でも可

# 画像の整列方法を選択できるセレクトボックスを作成
vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

# セレクトボックスの選択に応じて画像を整列
left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")


# Image Credit
# By @phonvanna (https://unsplash.com/photos/0g7BJEXq7sU)
# By @shotbyrain (https://unsplash.com/photos/rmkIqi_C3cA)
# By @zmachacek (https://unsplash.com/photos/ZN4CzqizIyI)
