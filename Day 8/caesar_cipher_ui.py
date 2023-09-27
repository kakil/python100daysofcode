import streamlit as st
from art import logo

# Function to perform Caesar Cipher
def caesar_cipher(text, shift, direction):
    # List of alphabet characters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Adjust shift based on direction
    if direction == "decode":
        shift = -shift  # Reverse the shift for decoding
    
    # Perform Caesar Cipher
    ciphered_text = ''
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            ciphered_text += alphabet[new_position]
        else:
            ciphered_text += char
    
    return ciphered_text


# Streamlit UI
st.title("Caesar Cipher Encoder/Decoder")
text = st.text_input("Enter your message:")
shift = st.slider("Select shift value:", min_value=1, max_value=25, value=3)
direction = st.selectbox("Select operation:", ("Encode", "Decode"))
result = ""

if st.button("Perform Operation"):
    result = caesar_cipher(text.lower(), shift, direction.lower())

st.write("Result:", result)  # Display the result