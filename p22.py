import pandas as pd
import streamlit as st

st.title('CAMERA BASED PROFILE CREATOR')
name=st.text_input('enter your name')
bio=st.text_area('enter short biography')
photo = st.camera_input('click a photo')
if st.button('create profile'):
    if name and bio and photo:
        st.success('profile created succesfull')
        st.image(photo,caption=name)
        st.write(bio)
else:
    st.error('please fill all fields and take a photo')
