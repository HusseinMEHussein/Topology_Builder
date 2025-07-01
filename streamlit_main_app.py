import pulp
import numpy as np
import pandas as pd

import streamlit as st



st.set_page_config(layout="wide")

# st.image("Hussein Hussein_Headshot_1.png", width=200,  caption="Sunrise by the mountains")


st.link_button("@ Hussein Hussein", "https://www.linkedin.com/in/husseinmehussein/")
# Target values
# ytarget = np.array([2482, 2466, 2448, 2436, 2374, 2356, 2338, 2310])  # N_indep_Freqx1 vector
# ytarget = np.array([2482, 2466, 2448, 2437, 2374, 2356, 2335, 2310])  # N_indep_Freqx1 vector KB233

# ytarget = np.array([2482, 2472, 2444, 2375, 2358, 2336, 2310])  # N_indep_Freqx1 vector %KB161


st.title("Filter Topology Builder ")
st.write("version 1.0.0")
st.write("© 2025 Hussein Hussein @ Skyworks Solutions")


text = "Please note that NPI approval is still needed!"
highlight_color =  "#ffff00"

highlighted_text = f"<span style='background-color:{highlight_color};'>{text}</span>"
st.markdown(highlighted_text, unsafe_allow_html=True)

