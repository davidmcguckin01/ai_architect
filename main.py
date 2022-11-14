import os
import replicate
import streamlit as st
from tinydb import TinyDB

db = TinyDB("data.json")

"""
# AI Interior Designer
In the form, you will inout an instruction and we will generate an image for you.
_We don't sell this data_
"""

instruction = st.text_input("Enter your instruction")

if st.button('Generate'):
    model = replicate.models.get("stability-ai/stable-diffusion")
    image = model.predict(prompt=instruction)
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    if instruction:
        db.insert({
            "instruction" : instruction, 
            "image" : image
        })
