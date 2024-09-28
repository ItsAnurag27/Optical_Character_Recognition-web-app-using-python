import easyocr as ocr  
import streamlit as st  #web application
from PIL import Image #Image Process
import numpy as np #MAths

st.title("Easy OCR - Extract Text from Images")


st.markdown("// Optical Character Recognition - Using `streamlit`//")

st.markdown("")


image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg' , 'Svg' , 'Gif'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() 

if image is not None:

    input_image = Image.open(image) 
    st.image(input_image) 

    with st.spinner("Hold on don`t move!!!! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] 


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
   
    st.balloons()
else:
    st.write("Upload an Image 👆🏻")







