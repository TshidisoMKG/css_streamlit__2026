# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("Hello2")

st.title("Title heading")

st.write("Hello, Streamlit!")

st.write("Has this changed")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")

st.markdown("Some text that you can write")