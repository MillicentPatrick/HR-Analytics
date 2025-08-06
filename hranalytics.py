# hranalytics.py
import streamlit as st
from utils.auth import display_login

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    display_login()
else:
    st.switch_page("pages/home.py")
