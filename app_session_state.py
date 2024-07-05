import streamlit as st


# st.session_stateを使わない場合、countの値が保持されない
# count = 0

# st.write("Counter:", count)

# if st.button("Increment"):
#     count += 1


# st.session_stateを使うと、スクリプトの上から再実行されても値が保持される
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

st.write("Counter:", st.session_state['counter'])

if st.button('Increment'):
    st.session_state['counter'] += 1
    st.rerun()
