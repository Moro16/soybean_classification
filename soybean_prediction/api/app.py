import streamlit as st
from PIL import Image
import requests

# Set page tab display
st.set_page_config(
   page_title="Simple Image Uploader",
   page_icon= '🖼️',
   layout="wide",
   initial_sidebar_state="expanded",
)

# import style
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
url = 'https://bean-prediction-image-3-479795464782.southamerica-east1.run.app'


# App title and description
st.markdown('### 🌽🫘Soybean and corn quality analysis🫘🌽')
st.markdown('''
            > In our project, we developed deep learning models to help farmers detect low-quality soybeans and corn grains

            > * The models were created using convolutional neural networks
            > * For soybeans, the model has an accuracy of 90.48%
            > * For corn, the model has an accuracy of 69.85%
            ''')

st.markdown("---")

### Create a native Streamlit file upload input

tab1, tab2 = st.tabs(["Soy 🫘", "Corn 🌽"])

with tab1:

    st.markdown("### SOYBEAN recognition 🫘")
    img_file_buffer_soy= st.file_uploader('Upload an image', key='soybean')

    if img_file_buffer_soy is not None:
        col1, col2= st.columns(2)

        with col1:
            ### Display the image user uploaded
            st.markdown("### Here's the image you uploaded")
            st.image(Image.open(img_file_buffer_soy))

        with st.spinner("Wait for it..."):
            ### Get bytes from the file buffer
            img_bytes = img_file_buffer_soy.getvalue()

            ### Make request to  API (stream=True to stream response as bytes)
            res = requests.post(url + "/upload_image_sb", files={'img': img_bytes})


        with col2:
            if res.status_code == 200:
            ### Display the image returned by the API
                st.markdown("### Results")
                st.metric("Class", res.json()['class'])
                st.metric("Accuracy", res.json()['accuracy'])

            else:
                st.markdown("**Oops**, something went wrong 😓 Please try again.")
                print(res.status_code, res.content)


with tab2:

    st.markdown("### CORN recognition 🌽")
    img_file_buffer_corn = st.file_uploader('Upload an image', key='corn')

    if img_file_buffer_corn is not None:
        col3, col4= st.columns(2)

        with col3:
            ### Display the image user uploaded
            st.markdown("### Here's the image you uploaded")
            st.image(Image.open(img_file_buffer_corn))

        with st.spinner("Wait for it..."):
            ### Get bytes from the file buffer
            img_bytes = img_file_buffer_corn.getvalue()

            ### Make request to  API (stream=True to stream response as bytes)
            res = requests.post(url + "/upload_image_corn", files={'img': img_bytes})


        with col4:
            if res.status_code == 200:
            ### Display the image returned by the API
                st.markdown("### Results")
                st.metric("Class", res.json()['class'])
                st.metric("Accuracy", res.json()['accuracy'])

            else:
                st.markdown("**Oops**, something went wrong 😓 Please try again.")
                print(res.status_code, res.content)
