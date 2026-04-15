import streamlit as st
from utils import (
    initialize_session_state,
    render_auth_sidebar,
    render_sidebar_footer,
    render_page_footer,
)

initialize_session_state()

st.set_page_config(page_title="Report")

st.markdown("# Report")
st.sidebar.header("Report")

render_auth_sidebar()
render_sidebar_footer()

st.write(
    """
    Here is a page with a report on it.
    """
)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.write(
    """
    Look at those numbers. Amazing.
    """
)

render_page_footer()