import streamlit as st

st.title("Dashboard")

def run_script():
    print("masterclass")
    print("Script running")

if st.button("Run script"):
    run_script()
    st.bar_chart()
