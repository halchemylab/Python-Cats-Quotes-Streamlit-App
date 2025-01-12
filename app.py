import streamlit as st
import requests

# ZenQuotes API URL
ZEN_QUOTES_URL = "https://zenquotes.io/api/random"

# The Cat API URL
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

# Function to fetch a quote
def fetch_quote():
    response = requests.get(ZEN_QUOTES_URL)
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f'"{quote}" - {author}'
    else:
        return "Failed to fetch a quote. Try again!"

# Function to fetch a random cat image
def fetch_cat_image():
    response = requests.get(CAT_API_URL)
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']
    else:
        return None

# Streamlit App
def main():
    st.title("Inspirational Cat Quotes App 🐾")
    st.write("Click the button to generate an inspirational quote paired with an adorable cat picture!")

    # Centering everything below the title
    with st.container():
        # Button to generate content
        if st.button("Generate Quote"):
            # Fetch quote
            quote = fetch_quote()
            
            # Use markdown to adjust the font size for the quote
            st.markdown(f"<h2 style='text-align: center; font-size: 36px;'>{quote}</h2>", unsafe_allow_html=True)

            # Fetch cat image
            cat_image_url = fetch_cat_image()
            if cat_image_url:
                st.image(cat_image_url)
            else:
                st.error("Failed to fetch a cat image. Try again!")

if __name__ == "__main__":
    main()