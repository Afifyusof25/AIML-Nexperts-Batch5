import streamlit as st
 
st.title("First Streamlit app")
 
st.write("Helloww. I am here to build apps!")
 
st.write("Helloww. I am here to build apps!")

name = st.text_input("What is your name?")

age = st.slider("How old are you?", 1, 100, 25)

if name:
    st.write(f"Nice to meet you, {name}!")