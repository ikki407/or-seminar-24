import streamlit as st


with st.echo():
    # このブロック内のすべてのコードはコードブロック画面に表示され、実行されます。
    def get_user_name():
        return 'John'

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# そして、コードブロック画面に表示されない状態に戻ります
foo = 'bar'
st.write('Done！')
