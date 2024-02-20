import streamlit as st
st.set_page_config(page_title='My web app')
st.header("my web site")
st.image('https://picsum.photos/500/400')
st.subheader("เว็บส่วนตัว")
col1,col2,col3 = st.columns([1,1,1])
with col1:
    text = st.text_input("prompt: ")
    if text :
        st.write(f'กำลังสร้างภาพ.... "{text}"')
        st.image('https://picsum.photos/400/200')
        b = st.button('จะไปต่อหรือ...')        