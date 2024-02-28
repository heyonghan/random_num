import streamlit as st
import random

# 设置页面标题
st.title('随机数生成器')

# 创建输入框让用户输入随机数的上限和下限
lower_bound = st.number_input('输入随机数下限:', value=0.0, step=1.0)
upper_bound = st.number_input('输入随机数上限:', value=100.0, step=1.0)

# 创建一个按钮，当点击时生成随机数
if st.button('生成随机数'):
    if lower_bound < upper_bound:
        # 生成随机数并保留两位小数
        random_number = round(random.uniform(lower_bound, upper_bound), 2)
        st.write(f'生成的随机数是: {random_number}')
    else:
        st.error('随机数下限必须小于上限。')
