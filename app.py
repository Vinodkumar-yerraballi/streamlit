import streamlit as st
from balance import user_amount_information

st.title(body='_Welcome to the_ :red[ABC] Bank')

import streamlit as st

# ---------- INITIAL SETUP ----------
st.set_page_config(page_title="Mini Bank", layout="centered")

# Define the user name
user_name='Bob'


# User_password
user_password='1234'


# user amount
user_amount=45000



# Create text to recevied the password 
user_login=st.text_input('Enter your pin',type="password", max_chars=4)

# Login button
login_button=st.button('login')

# Condition if login password and user password is equal return to welcome page and else getting error

if login_button:
    # Condition
    if user_login==user_password:
        st.success(f'Hi {user_name} welcome to bank service')
        st.success('Have a nice day')

    else:
        st.warning(f'❌ Wrong password entered {user_name}')

# Define the columne with buttons
left_1,left_2=st.columns(2)

# define the left_1 button for balance enquery
# if the login password equal to return to current balance amount

if user_login==user_password:
    # if click the left_1 button
    if left_1.button('Balance enquery',use_container_width=True):
        # Return to balance amount
        st.success(f'Your current balace ${user_amount}')
        st.success('Have a nice day')


# Again condition checking to create a button for change password
if  user_login==user_password:

    # Create change password button
    if left_1.button('Change password',use_container_width=True):
        st.session_state.update_password = True  # Store that the user clicked Withdraw
        # If withdraw section should be shown:
    if st.session_state.get("update_password", False):

        # Create a new input for the update password
        update_password=st.text_input(
            'Enter New Password',
            type='password',
            max_chars=4
            )
        
        # Define the another submit function
        submit_button=st.button('submit')

        # Clicked the submit button
        if submit_button:
            # Hide after submit
            st.session_state.update_password = False    
            st.success(f"✅ {update_password} New password changed successfully!")
            st.success('Have a nice day')


# Again checking the condition
if user_login == user_password:

    # Withdraw button
    if left_2.button("Withdraw", use_container_width=True):
        # Store that the user clicked Withdraw
        st.session_state.show_withdraw = True  

    # If withdraw section should be shown:
    if st.session_state.get("show_withdraw", False):
        
        #Getting the input amount 
        input_amount = st.number_input(
            "Enter your amount",
            min_value=0,
            value=0,
            placeholder="Enter your amount..."
        )

        # Create the submit withdraw button
        submit_withdraw = st.button("Submit Withdraw")

        # Now call your function
        if submit_withdraw:
            # define the function 
            user_amount_information(user_amount, input_amount)
            # Hide after submit
            st.session_state.show_withdraw = False
            st.success('Have a nice day')
     


# Again checking condition for deposti the amoutn

if user_login==user_password:

    # create a button for the deposti
    if left_2.button("Deposit",use_container_width=True):
        st.session_state.Deposit_amount = True

    if st.session_state.get("Deposit_amount",False):
        # Getting amount from the user
        user_dposit=st.number_input(
            "Enter amount deposit",
            min_value=0,
            value=0,
            placeholder="Enter deposit amount"

        )

        #Create a button for the deposit amount
        dposite_amount_button=st.button("Deposite_amount",use_container_width=True)


        # Click the the button
        if dposite_amount_button:
            # Hide after submit
            st.session_state.Deposit_amount = False 

            # Calculate the amount user_deposti and user amount
            final_amount=user_dposit + user_amount

            # Display total amount deposit and user amount
            st.success (f'✅ Amount Deposited Successfully!\n💰 Final Balance: ₹{final_amount}')
            st.success('Have a nice day')




        
