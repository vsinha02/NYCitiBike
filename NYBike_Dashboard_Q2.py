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
st.title('New York City Bikes Dashboard - Q2')
# st.markdown(
#     "<h1 style='text-align: center;'>New York City Bikes Dashboard</h1>",
#     unsafe_allow_html=True
# )
####################### Import data #########################################

col_1, col_2 = st.columns((2))
with col_1:
  filepath = '/Users/vineetasinha/Documents/workspace/NYCitiBike/top20_Q2.csv'
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
  filepath = '/Users/vineetasinha/Documents/workspace/NYCitiBike/Q2_first_part.csv'

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

#### Line chart for Q1_second_part.csv ###########

col_3, col_4, col_5 = st.columns((3))
with col_3:
  new_df2 = pd.read_csv('/Users/vineetasinha/Documents/workspace/NYCitiBike/Q2_second_part.csv')
  fig_3 = make_subplots(specs = [[{"secondary_y": True}]])
  make_subplots()
  fig_3.add_trace(
  go.Scatter(x = new_df2['date'], y = new_df2['bike_rides_daily'], name = 'Daily bike rides', 
  marker={'color': new_df2['bike_rides_daily'],'color': 'blue'}),
  secondary_y = False)
  fig_3.add_trace(
  go.Scatter(x=new_df2['date'], y = new_df2['AvgTemp'], name = 'Daily temperature', 
  marker={'color': new_df2['AvgTemp'],'color': 'red'}),
  secondary_y=True)
  st.plotly_chart(fig_3, use_container_width=False)


#### Line chart for Q1_third_part.csv ###########

with col_4:    
  new_df3 = pd.read_csv('/Users/vineetasinha/Documents/workspace/NYCitiBike/Q2_third_part.csv')
  fig_4 = make_subplots(specs = [[{"secondary_y": True}]])
  make_subplots()
  fig_4.add_trace(
  go.Scatter(x = new_df3['date'], y = new_df3['bike_rides_daily'], name = 'Daily bike rides', 
  marker={'color': new_df3['bike_rides_daily'],'color': 'blue'}),
  secondary_y = False)
  fig_4.add_trace(
  go.Scatter(x=new_df3['date'], y = new_df3['AvgTemp'], name = 'Daily temperature', 
  marker={'color': new_df3['AvgTemp'],'color': 'red'}),
  secondary_y=True)
  st.plotly_chart(fig_4, use_container_width=False)


#### Line chart for Q1_fourth_part.csv ###########

with col_5:    
  new_df4 = pd.read_csv('/Users/vineetasinha/Documents/workspace/NYCitiBike/Q2_fourth_part.csv')
  fig_5 = make_subplots(specs = [[{"secondary_y": True}]])
  make_subplots()
  fig_5.add_trace(
  go.Scatter(x = new_df4['date'], y = new_df4['bike_rides_daily'], name = 'Daily bike rides', 
  marker={'color': new_df4['bike_rides_daily'],'color': 'blue'}),
  secondary_y = False)
  fig_5.add_trace(
  go.Scatter(x=new_df4['date'], y = new_df4['AvgTemp'], name = 'Daily temperature', 
  marker={'color': new_df4['AvgTemp'],'color': 'red'}),
  secondary_y=True)
  st.plotly_chart(fig_5, use_container_width=False)
