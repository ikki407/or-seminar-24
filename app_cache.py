import streamlit as st
import time


@st.cache_data
def load_large_data(data_size):
    # 高コストな処理を実行し、データを返す
    time.sleep(data_size)
    return list(range(data_size))


# load_large_dataを実行する
start = time.time()
d1 = load_large_data(data_size=10)
st.markdown('**d1がロードされました（関数が実行されました）**')
st.write(f'経過時間：{time.time()-start:.2f}秒')

# load_large_dataを実行せずにキャッシュされた値を返すため、d1 == d2
start = time.time()
d2 = load_large_data(data_size=10)
st.markdown('**d2がロードされました（関数は実行されず、キャッシュされた値が返されました）**')
st.write(f'経過時間：{time.time()-start:.2f}秒')

# 異なる引数なので、load_large_data関数が実行される
start = time.time()
d3 = load_large_data(data_size=5)
st.markdown('**d3がロードされました（関数が実行されました）**')
st.write(f'経過時間：{time.time()-start:.2f}秒')


# この関数のキャッシュされたエントリをすべてクリアする
load_large_data.clear()

# *すべて*のメモリ上またはディスク上のキャッシュされた関数の値をクリアする
# st.cache_data.clear()
