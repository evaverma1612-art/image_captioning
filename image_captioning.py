import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Image Captioning AI", page_icon="🖼️")
st.title("🖼️ AI Image Captioning")
st.write("Upload an image and the AI will describe what it sees.")

@st.cache_resource
def load_captioning_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_captioning_model()

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    with st.spinner('Generating caption...'):
        text_inputs = processor(image, return_tensors="pt")
        output = model.generate(**text_inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        
    st.success(f"**Caption:** {caption.capitalize()}")
