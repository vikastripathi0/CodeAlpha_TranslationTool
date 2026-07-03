# app.py
# This is a simple Language Translation Tool.
# We use Streamlit to make a webpage, and deep-translator to do the actual translation.

# Step 1: Import the tools (libraries) we installed
import streamlit as st
from deep_translator import GoogleTranslator

# Step 2: Set the title of our webpage
st.title("🌍 Language Translation Tool")
st.write("Type text, choose languages, and get an instant translation!")

# Step 3: A dictionary of language name -> language code
# (deep-translator needs short codes like 'en', 'hi', 'fr' etc.)
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt"
}

# Step 4: Create a text box where the user types what they want translated
input_text = st.text_area("Enter text to translate:", height=150)

# Step 5: Create two dropdown menus - one for source language, one for target
col1, col2 = st.columns(2)  # this puts the two dropdowns side by side

with col1:
    source_lang_name = st.selectbox("From:", list(languages.keys()), index=0)

with col2:
    target_lang_name = st.selectbox("To:", list(languages.keys()), index=1)

# Step 6: Create a button. When clicked, we do the translation.
if st.button("Translate"):
    # Check if the user actually typed something
    if input_text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        # Convert the language names to their codes
        source_code = languages[source_lang_name]
        target_code = languages[target_lang_name]

        # Step 7: Use GoogleTranslator to do the translation
        try:
            translated = GoogleTranslator(source=source_code, target=target_code).translate(input_text)

            # Step 8: Show the result on the screen
            st.success("Translation:")
            st.write(translated)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# Step 9 (Bonus): Add a small footer
st.markdown("---")
st.caption("Built with Python, Streamlit & deep-translator")