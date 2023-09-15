import streamlit as st

# Create a sidebar with links to the different sections of the portal.
with st.sidebar:
    st.title("AutoML")
    st.info("By Akshith Chowdary")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnxi_YIKmP9dAESxenlz-fl5En_rFFSgdYtw&usqp=CAU", width=250)
    choose = st.radio("Options", ['Upload', 'Profiling', 'Model Building', 'Download Model'])
    st.info("This application will help you to explore your data, build and train a ML Model, save your model.")

