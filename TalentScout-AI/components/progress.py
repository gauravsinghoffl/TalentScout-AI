import streamlit as st

def render_progress(step,total):

    progress = step / total

    st.progress(progress)
