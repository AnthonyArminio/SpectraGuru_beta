import streamlit as st;

st.title("Test Script")

st.write("Hello World")

if "button_counter" not in st.session_state:
    st.session_state["button_counter"] = 0

button = st.button("Try me", help="test button")
reset_button = st.button("Reset", help="reset button count")

if (button):
    st.session_state["button_counter"] += 1
    for i in range(st.session_state["button_counter"]):
        st.write("...")

if (reset_button):
    st.session_state["button_counter"] = 0