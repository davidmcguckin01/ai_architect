import os
import replicate
import streamlit as st
from tinydb import TinyDB
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

db = TinyDB("data.json")

"""
# Welcome to AI Architect
Input your prompt and we will generate a design for you.
_Process may take up to 10 seconds_
"""

instruction = "Realistic architectural rendering of " + st.text_input("Enter your instruction") + ", highly detailed realistic modern Home with a view, Photorealistic, rendered in unreal engine, ultradetail"

print(instruction)

if st.button('Generate'):
    model = replicate.models.get("stability-ai/stable-diffusion")
    image = model.predict(prompt=instruction)
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    if instruction:
        db.insert({
            "instruction" : instruction, 
            "image" : image
        })
