# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:56:51 2026

@author: Tshidiso
"""

import streamlit as st

st.title("Tshidiso Mokgele | Student | Research |")

st.write("Hello, Streamlit!")

st.write("Has this changed")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")


st.markdown("Some text that you can write")

