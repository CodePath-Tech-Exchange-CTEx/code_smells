import streamlit as st
from utils import (
    initialize_session_state,
    render_auth_sidebar,
    render_sidebar_footer,
    render_page_footer,
)

initialize_session_state()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit!")

render_auth_sidebar()
render_sidebar_footer()

st.markdown(
    """
    This website has a lot of redundant code. Can you find it and create a utility file which contains the redundancies?
    """
)

render_page_footer()