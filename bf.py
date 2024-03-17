import streamlit as st
import bfc

bfcode=st.text_input('输入bf代码')

st.text(bfc.bfc(bfcode))