import streamlit as st


st.title("Hello, Streamlit!")  # タイトル表記

st.text("Fixed width text")  # 固定幅テキスト
st.markdown("Markdown, _Markdown_, $Markdown$, **Markdown**")  # マークダウン
st.caption("図1: ORセミナー")  # キャプション
st.latex(r""" e^{i\pi} + 1 = 0 """)  # LaTeX


def test(x: int) -> int:
    """
    This is a test function that returns the value 42.

    Arguments:
    x: int - an parameter
    """
    return 42


st.write(test)  # df, err, func, torch, etc.
st.write(["st", "is <", 3])  # リスト表記

# Github flavored markdown
st.title("My title")
st.header("My header", divider='red')
st.subheader("My sub", divider='rainbow')

# コードブロック
st.code("for i in range(8): foo()")
st.code("""
        for i in range(8):
            foo()
        """)
