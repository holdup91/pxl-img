# pixelate_app.py

import streamlit as st
from PIL import Image, ImageFilter

def pixelate_image(image, pixel_size):
    pixelated_image = image.resize(
        (image.width // pixel_size, image.height // pixel_size),
        resample=Image.NEAREST
    )
    pixelated_image = pixelated_image.resize(
        (image.width, image.height),
        resample=Image.NEAREST
    )
    return pixelated_image

def main():
    st.title("Image Pixelation App")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display original image
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)

        # Pixelation settings
        pixel_size = st.slider("Select pixel size", 1, 50, 10)

        # Pixelate the image
        pixelated_image = pixelate_image(original_image, pixel_size)

        # Display pixelated image
        st.image(pixelated_image, caption="Pixelated Image", use_column_width=True)

if __name__ == "__main__":
    main()
