import streamlit as st
from acc_book import Account

# Persist data across reloads
if "account" not in st.session_state:
    st.session_state.account = Account(0)

account = st.session_state.account

st.title("Account Book Manager")

menu = st.sidebar.selectbox("Menu", ["Deposit", "Withdraw", "Balance", "History"])

# DEPOSIT
if menu == "Deposit":
    st.subheader("Deposit Money")
    amount = st.number_input("Enter amount", min_value=0.0)

    if st.button("Deposit"):
        success, msg = account.deposit(amount)
        if success:
            st.success(msg)
        else:
            st.error(msg)

# WITHDRAW
elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    amount = st.number_input("Enter amount", min_value=0.0)

    if st.button("Withdraw"):
        success, msg = account.withdraw(amount)
        if success:
            st.success(msg)
        else:
            st.error(msg)

# BALANCE
elif menu == "Balance":
    st.subheader("Current Balance")
    st.metric("Balance", f"${account.view_balance()}")

# HISTORY
elif menu == "History":
    st.subheader("Transaction History")
    history = account.view_history()

    if history:
        for t in history:
            st.write(t)
    else:
        st.info("No transactions yet")
