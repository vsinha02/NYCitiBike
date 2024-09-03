import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from streamlit_keplergl import keplergl_static 
import matplotlib.pyplot as plt
from datetime import datetime as dt 

st.set_page_config(
    page_title='New York City Bikes Dashboard',  # Page title
    page_icon='🚴',  # Page icon (optional)
    layout='wide',  # Page layout (can be 'wide' or 'centered')
    initial_sidebar_state='expanded',  # Initial state of the sidebar (optional)
)

st.title('New York City Bikes Dashboard - Q1')

# st.markdown(
#     "<h1 style='text-align: center;'>New York City Bikes Dashboard</h1>",
#     unsafe_allow_html=True
# )
####################### Import data #########################################

col_1, col_2 = st.columns((2))
with col_1:
  filepath = '/Users/vineetasinha/Documents/workspace/NYCitiBike/top20.csv'
  top_20 = pd.read_csv(filepath)
  fig = go.Figure(go.Bar(x = top_20['start_station_name'], y = top_20['value'], marker = {'color': top_20['value'],'colorscale': 'Blues'}))
  fig.update_layout(
    width=500,  # Fixed width in pixels
    height=500,  # Fixed height in pixels
    margin=dict(l=20, r=20, t=50, b=20)
  )
  st.plotly_chart(fig, use_container_width = False)

## Line chart for Q1_first_part.csv  ###########

with col_2:
  filepath = '/Users/vineetasinha/Documents/workspace/NYCitiBike/new_df1.csv'

  new_df1 = pd.read_csv(filepath)
  fig_2 = make_subplots(specs = [[{"secondary_y": True}]])
  make_subplots()
  fig_2.add_trace(
  go.Scatter(x = new_df1['date'], y = new_df1['bike_rides_daily'], name = 'Daily bike rides', 
  marker={'color': new_df1['bike_rides_daily'],'color': 'blue'}),
  secondary_y = False)
  fig_2.add_trace(
  go.Scatter(x=new_df1['date'], y = new_df1['AvgTemp'], name = 'Daily temperature', 
  marker={'color': new_df1['AvgTemp'],'color': 'red'}),
  secondary_y=True)
  fig.update_layout(
    width=500,  # Fixed width in pixels
    height=400,  # Fixed height in pixels
    margin=dict(l=20, r=20, t=50, b=20)
  )
  st.plotly_chart(fig_2, use_container_width=False)



