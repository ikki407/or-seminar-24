import streamlit as st


st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
