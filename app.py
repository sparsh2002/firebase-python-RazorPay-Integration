import streamlit as st

#importing pages 
from home_page import show_home_page
from firebase_page import show_firebase_page
from razorpay_page import show_razorpay_page
page = st.sidebar.selectbox("Menu",("Home","FireBase","RazorPay"))

if page=='RazorPay':
    show_razorpay_page()

elif page=='FireBase':
    show_firebase_page()

else:
    show_home_page()