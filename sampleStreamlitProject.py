import streamlit as st

st.write("""
# Sample Streamlit Project
This is a sample project.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("You can organize your app by columns if you want")

with col3:
    st.write("But then again, you don't have to. It's just a suggestion")
