import streamlit as st
from bs_model import bs_call_price, bs_put_price

# Page configuration
st.set_page_config(
    page_title="Black–Scholes Pricer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("Black–Scholes European Option Pricer")

# Sidebar inputs
st.sidebar.header("Model Inputs")
S = st.sidebar.number_input(
    label="Stock price (S)", min_value=0.0, value=100.0, step=1.0
)
K = st.sidebar.number_input(
    label="Strike price (K)", min_value=0.0, value=100.0, step=1.0
)
T = st.sidebar.number_input(
    label="Time to expiry (years)", min_value=0.0, max_value=5.0,value=1.0, step=0.01
)
r = st.sidebar.number_input(
    label="Risk-free rate (r)", min_value=0.0, value=0.05, step=0.001, format="%.3f"
)
sigma = st.sidebar.number_input(
    label="Volatility (σ)", min_value=0.0, value=0.2, step=0.01, format="%.2f"
)

# Calculate button (disabled when T == 0)
if T > 0:
    if st.sidebar.button("Calculate"):
        # Compute option prices
        call_price = bs_call_price(S, K, T, r, sigma)
        put_price = bs_put_price(S, K, T, r, sigma)

        # Display results side-by-side
        col1, col2 = st.columns(2)
        col1.metric("Call price", f"${call_price:.2f}")
        col2.metric("Put price", f"${put_price:.2f}")
else:
    st.sidebar.button("Calculate", disabled=True)
    st.sidebar.write("⏳ Time to expiry must be > 0")
