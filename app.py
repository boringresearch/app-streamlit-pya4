import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -- Set page config
apptitle = 'A4 simulation'

st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")

# Title the app
st.title('A4 Simulation')

st.sidebar.markdown("## Select the page size")

# -- Create sidebar for plot controls
st.sidebar.markdown('## Set figure width')
width = st.sidebar.slider('width inches', 0.01, 15.00, 11.69)  # min, max, default

st.sidebar.markdown('## Set figure height')
height = st.sidebar.slider('height inches', 0.01, 15.00, 8.27)  # min, max, default


f = plt.figure(figsize=(10,3))


st.subheader('A4')

fig = plt.figure(figsize=(8.27,11.69))
st.pyplot(fig, clear_figure=True)
ax = fig.add_subplot(121)
x = np.linspace(0,4,1000)
ax.plot(x, np.sin(x))
ax2.plot(x, np.cos(x), 'r:')

fig = plt.figure(figsize=(height,width))
st.pyplot(fig, clear_figure=True)

