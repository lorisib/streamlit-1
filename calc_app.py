import streamlit as st

num1 = st.number_input("please enter a number")
num2 = st.number_input("please enter a secont number")

operation = st.selectbox(
    'choose eopration',
    ('No option','Add', 'Subtract','Divide', 'Multiply'))



if operation=='Add':
    st.write(num1 + num2)
elif operation =='Subtract':
    st.write(num1 - num2)
elif operation=='Divide':
    st.write(num1 / num2)
elif operation=='Multiply':
    st.write(num1 + num2)
else:
    st.write('no operation')
