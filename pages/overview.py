import streamlit as st
from utils import (
    initialize_session_state,
    render_auth_sidebar,
    render_sidebar_footer,
    render_page_footer,
)

initialize_session_state()

st.set_page_config(page_title="Overview")

st.markdown("# Overview")
st.sidebar.header("Overview")

render_auth_sidebar()
render_sidebar_footer()

st.write(
    """Here is a page with a site overview.

    This site has one main page (app) and three pages (about, overview, and report).

    All of them have some redundant code that can be abstracted out to make changes easier in the future.
    """
)

render_page_footer()