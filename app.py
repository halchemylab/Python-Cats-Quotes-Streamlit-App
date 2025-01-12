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

    # Button to generate content
    if st.button("Generate Quote"):
        # Fetch quote
        quote = fetch_quote()
        st.subheader("Inspirational Quote:")
        st.write(quote)

        # Fetch cat image
        cat_image_url = fetch_cat_image()
        if cat_image_url:
            st.image(cat_image_url, caption="Here's some feline cuteness to brighten your day!")
        else:
            st.error("Failed to fetch a cat image. Try again!")

if __name__ == "__main__":
    main()