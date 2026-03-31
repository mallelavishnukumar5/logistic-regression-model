import streamlit as st
import pandas as pd
import pickle

st.markdown("""
<style>

/* Main app background */
[data-testid="stAppViewContainer"] {
    background-color: #f4f8ff;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #eaf2ff;
}

/* Optional: make text darker */
body {
    color: #000000;
}

.title{
    font-size:85px;
    font-weight:800;
    color:#2E86C1;
    text-align:center;
}

.subtitle{
    font-size:22px;
    color:gray;
    text-align:center;
}

.info-box{
    background-color:#eef5ff;
    padding:25px;
    border-radius:10px;
    margin-bottom:20px;
}

.result-high{
    background-color:#f8d7da;
    padding:25px;
    border-radius:10px;
    font-size:24px;
    color:#721c24;
    text-align:center;
}

.result-low{
    background-color:#d4edda;
    padding:25px;
    border-radius:10px;
    font-size:24px;
    color:#155724;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="result-low">✅ Low Risk: Patient is unlikely to have Diabetes</div>',
            unsafe_allow_html=True
        )
