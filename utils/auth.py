import streamlit as st

# Placeholder function for authentication (non-persistent)
def login_user(username, password):
    # Simulated credential check (replace with real logic)
    return username == "admin" and password == "admin123"

def display_login():
    st.sidebar.subheader("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if login_user(username, password):
            st.session_state['authenticated'] = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials.")
