import streamlit as st

COMPANY_NAME = "Fake Company LLC Inc."
COMPANY_ADDRESS = "1600 Amphitheatre Parkway Mountain View, CA 94043"
COMPANY_COPYRIGHT = "This site is copyright Fake Company LLC Inc., 2024"
COMPANY_LINKS = """
[Google](https://google.com)

[Gemini](https://gemini.google.com)

[Streamlit Docs](https://docs.streamlit.io/)
"""


def initialize_session_state():
    """Initialize login state if not already set."""
    if st.session_state.get("logged_in") is None:
        st.session_state["logged_in"] = False


def login():
    """Set user as logged in."""
    st.session_state.logged_in = True


def logout():
    """Set user as logged out."""
    st.session_state.logged_in = False


def render_auth_sidebar():
    """Render authentication status and buttons in sidebar."""
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", key="logout", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", key="login", on_click=login)


def render_sidebar_footer():
    """Render copyright footer in sidebar."""
    st.sidebar.write(COMPANY_COPYRIGHT)


def render_company_info():
    """Render company info expander."""
    with st.expander("Company Info"):
        st.write(f"{COMPANY_NAME} is located at {COMPANY_ADDRESS}")


def render_links():
    """Render links expander."""
    with st.expander("Links"):
        st.markdown(COMPANY_LINKS)


def render_page_footer():
    """Render company info and links footers."""
    render_company_info()
    render_links()