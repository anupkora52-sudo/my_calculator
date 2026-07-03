import streamlit as st

st.title("💰 Simple Interest Calculator")

# User inputs
principal = st.number_input("Enter the Principal Amount (₹)", min_value=0.0, value=1000.0)
rate_of_interest = st.number_input("Enter the Rate of Interest (%)", min_value=0.0, value=10.0)
years = st.number_input("Enter the Number of Years", min_value=0, value=1)
months = st.number_input("Enter the Number of Months", min_value=0, max_value=11, value=0)

# Calculate button
if st.button("Calculate"):
    time = years + (months / 12)

    # Simple Interest Formula
    interest = (principal * rate_of_interest * time) / 100
    maturity_amount = principal + interest

    st.success(f"Simple Interest: ₹{interest:.2f}")
    st.info(f"Maturity Amount: ₹{maturity_amount:.2f}")