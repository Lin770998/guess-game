import random
import streamlit as st

st.title("猜数字小游戏")

# 初始化随机数
if "secret_num" not in st.session_state:
    st.session_state.secret_num = random.randint(1,100)
if "count" not in st.session_state:
    st.session_state.count = 0

st.write("我想好了一个1~100之间的数字，你来猜猜！")
guess = st.number_input("输入你的猜测：", min_value=1, max_value=100, step=1)
btn = st.button("提交猜测")

if btn:
    st.session_state.count += 1
    if guess < st.session_state.secret_num:
        st.info("猜小了！再试试")
    elif guess > st.session_state.secret_num:
        st.info("猜大了！再试试")
    else:
        st.success(f"🎉猜对啦！一共猜了{st.session_state.count}次")
        if st.button("重新开始"):
            del st.session_state.secret_num
            del st.session_state.count
            st.rerun()
