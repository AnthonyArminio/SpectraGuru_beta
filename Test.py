import streamlit as st

st.title("Test Script")
st.write("This script is to be used for testing only.")

if "count" not in st.session_state:
    st.session_state.count = 0

button = st.button("Test Button")
reset_button = st.button("Reset")

if (button):
    st.session_state.count += 1

if (reset_button):
    st.session_state.count = 0

for i in range(st.session_state.count):
    st.write("The button was pressed.")