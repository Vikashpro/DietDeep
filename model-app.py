import streamlit as st
from transformers import pipeline
from PIL import Image

# Hugging Face model
@st.cache_resource()
def load_model():
    return pipeline("image-classification", model="ewanlong/food_type_image_detection")

pipe = load_model()

st.title("🍔 Food Image Classifier")
st.write("Upload an image to classify the type of food.")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    
    new_size = (256, 256)
    image.thumbnail(new_size)

    
    st.image(image, caption="Uploaded Image", use_column_width=True)

    
    with st.spinner("Classifying..."):
        results = pipe(image)

    
    st.subheader("Predictions:")
    for item in results:
        st.write(f"**{item['label'].capitalize()}** - {item['score']*100:.2f}% confidence")
