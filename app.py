import streamlit as st
import requests
import base64

st.title("AI-Powered Clothing Analysis")
st.write("Upload an image to get outfit suggestions.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("Processing the image...")

    # Convert image to Base64
    def encode_image(image_file):
        return base64.b64encode(image_file.read()).decode("utf-8")

    base64_image = encode_image(uploaded_file)

    # Send request to AI model
    url = "https://clothing-ai-api.onrender.com/analyze"  # Replace with your actual API endpoint
    data = {"image": base64_image}
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            result = response.json().get("analysis", "No analysis received.")
            st.subheader("AI Suggestions:")
            st.write(result)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Failed to connect to AI API: {e}")