import streamlit as st

def main():
    #Title of the page
    st.title('Basic Web Calculator')
    # Let's define the values
    values=['Addition','Subtraction','Multiplication','Divison','Percentage']
    # Create dropdown box 
    box_selection=st.selectbox('What yout whant',values)
    # define the user input recive from the user
    t1=st.number_input('Insert frist number',min_value =0,value=None, placeholder="Type a number...")
    t2=st.number_input('Insert second number',min_value =0,value=None, placeholder="Type a number...")
    #Define the some function to addition 
    def add_values(a,b):
        if a is None and b is None:
            return 0
        return a + b
    # substraction values
    def subtraction_values(a,b):
        if a is None and b is None:
            return 0
        return a - b
    def multiplication(a,b):
        if a is None and b is None:
            return 0
        return a *b
    def division(a,b):
        if a is None and b is None:
            return 0
        return a//b
    def percentage(a,b):
        if a is None and b is None:
            return 0
        return round((a/b) *100)
    if st.button('Result'):
        if box_selection==values[0]:
            addition_result=add_values(t1,t2)
            result_1=round(addition_result)
            st.write('You  selected',box_selection)
            st.write('The Addition of the two numbers is ',result_1)
    
        elif box_selection == values[1]:
            sub_values=subtraction_values(t1,t2)
            st.write('You  selected',box_selection)
            st.write('The Subtraction of the two numbers is',sub_values)
        elif box_selection==values[2]:
            multiflication_values=multiplication(t1,t2)
            st.write('You  selected',box_selection)
            st.write('The Multiflication of the two numbers is',multiflication_values)
        elif box_selection==values[3]:
            division_values=division(t1,t2)
            st.write('You  selected',box_selection)
            st.write('The division of the two numbers is',division_values)
        elif box_selection==values[4]:
            percentage_values = percentage(t1,t2)
            st.write('You  selected',box_selection)
            st.write('The Percentage of the two number is',percentage_values,'%')

        else:
            print('Error')
        st.balloons()



    
    




if __name__=='__main__':
    main()