# Let's define the user amnout 
import streamlit as st
user_amount=45000

def user_amount_information(user_amount,input_amount):
    remain_amount=user_amount-input_amount
    
    if user_amount <= 0:
        st.warning('Please enter amount greater then 0')
    elif remain_amount < 0:
        st.error("Insufficient balance!")
    else:
        st.success(f'The remaining amount in your account is: ₹{remain_amount}')
    


