import pulp
import numpy as np
import pandas as pd

import streamlit as st



import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

st.set_page_config(layout="wide")

# st.image("Hussein Hussein_Headshot_1.png", width=200,  caption="Sunrise by the mountains")


st.link_button("@ Hussein Hussein", "https://www.linkedin.com/in/husseinmehussein/")


st.title("Filter Topology Builder ")
st.write("version 1.0.0")
st.write("© 2025 Hussein Hussein @ Skyworks Solutions")


text = "beta version"
highlight_color =  "#ffff00"

highlighted_text = f"<span style='background-color:{highlight_color};'>{text}</span>"
st.markdown(highlighted_text, unsafe_allow_html=True)




# Load resonator images
series_img = Image.open("images/Series_Resonator.png")
shunt_img = Image.open("images/Shunt_Resonator.png")

# Function to generate a schematic image
def generate_schematic(start_with_series, num_resonators):
    images = []
    for i in range(num_resonators):
        if (i % 2 == 0 and start_with_series) or (i % 2 == 1 and not start_with_series):
            img = series_img.copy()
            label = f"S{i+1}"
        else:
            img = shunt_img.copy()
            label = f"S{i+1}"
        # Add label to image
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((10, 10), label, fill="black", font=font)
        images.append(img)

    # Combine images horizontally
    total_width = sum(img.width for img in images)
    max_height = max(img.height for img in images)
    combined = Image.new("RGB", (total_width, max_height), "white")

    x_offset = 0
    for img in images:
        combined.paste(img, (x_offset, 0))
        x_offset += img.width

    return combined

num_resonators = st.number_input("Enter the number of resonators:", min_value=1, step=1)

if st.button("Generate Circuit Schematics"):
    schematic_series = generate_schematic(True, num_resonators)
    schematic_shunt = generate_schematic(False, num_resonators)

    # Save images
    schematic_series.save("circuit_starting_with_series.png")
    schematic_shunt.save("circuit_starting_with_shunt.png")

    # Display images
    st.subheader("Circuit starting with Series Resonator")
    st.image(schematic_series, use_container_width=True)

    st.subheader("Circuit starting with Shunt Resonator")
    st.image(schematic_shunt, use_container_width=True)

    st.success("Schematics generated and saved successfully.")
