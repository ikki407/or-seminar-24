import streamlit as st


# 実行を即座に停止する：
# st.stop()

# スクリプトを即座に再実行する：
# st.rerun()

# 複数のウィジェットをグループ化する：
with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    submitted = st.form_submit_button('Login')

if submitted:
    if username == 'aaa' and password == 'bbb':
        st.write('Logged in')
    else:
        st.write('Invalid username and/or password')
else:
    st.write('Please login')
