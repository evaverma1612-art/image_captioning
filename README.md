# AI Image Captioning (CODSOFT Task 3)

This application uses artificial intelligence to generate descriptive captions for uploaded images. It is built with Streamlit for the user interface and utilizes the Hugging Face `transformers` library, specifically the Salesforce BLIP image captioning model.

## Features

- Easy-to-use web interface for uploading images.
- Uses the `Salesforce/blip-image-captioning-base` model to analyze the image and generate a caption.
- Displays the uploaded image alongside the generated text description.

## Prerequisites

- Python 3.7+
- Streamlit
- Transformers (Hugging Face)
- PyTorch
- Pillow (PIL)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/evaverma1612-art/image_captioning.git
   cd image_captioning
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit transformers torch torchvision Pillow
   ```

## Usage

Run the Streamlit application:

```bash
streamlit run image_captioning.py
```

Navigate to the provided local URL (usually `http://localhost:8501`), upload an image (JPG, JPEG, or PNG), and wait for the AI to generate a caption.
