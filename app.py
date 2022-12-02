import streamlit as st
st.markdown("## Hariboll")
a = st.radio('choose',options=[1,2,3,4])
st.markdown(f"you chose {a}")