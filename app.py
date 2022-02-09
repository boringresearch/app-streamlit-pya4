import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -- Set page config
apptitle = 'A4 simulation'

st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")

# -- Default detector list
detectorlist = ['H1','L1', 'V1']

# Title the app
st.title('A4 Simulation')

st.sidebar.markdown("## Select the page size")

# -- Create sidebar for plot controls
st.sidebar.markdown('## Set figure width')
width = st.sidebar.slider('width inches', 0.1, 15, 11.69)  # min, max, default

st.sidebar.markdown('## Set figure height')
height = st.sidebar.slider('height inches', 0.1, 15, 8.27)  # min, max, default



st.subheader('A4')

fig = plt.figure(figsize=(11.69,8.27))
st.pyplot(fig, clear_figure=True)


fig = plt.figure(figsize=(width,height))
st.pyplot(fig, clear_figure=True)

