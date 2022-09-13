import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import pickle
import plotly.graph_objects as go

# https://plotly.com/python/mapbox-density-heatmaps/
@st.cache
def data(): 
    with open('st_no_sprayed.pkl', 'rb') as f:
        df = pickle.load(f)
    return df

df = data()
df1 = df.head(10)
df2 = df.iloc[10:]

st.sidebar.title('🦟 Identifying presence of West Nile Virus per Trap')
st.sidebar.info('## What if all trap areas were not sprayed?')

#px.set_mapbox_access_token(open('./.gitignore/.mapbox_token.txt').read())

fig = px.scatter_mapbox(df1, 
                        lat='Latitude', 
                        lon='Longitude', 
                        color='WnvPresent', 
                        zoom=9,
                        height=650,
                        title='''Density map of West Nile Virus if all trap area were NOT sprayed'''
                        )
fig.update_layout(mapbox_style="carto-positron", 
                  mapbox_center = {"lat": 41.85, "lon": -87.63})

fig.update(layout_coloraxis_showscale=False) # removes default color scale on the side
st.plotly_chart(fig, use_container_width=True)

for i in range(len(df2)):
    fig.add_trace(go.Scattergeo(df2, lat='Latitude', lon='Longitude', mode='markers'))
    # Sleep for a moment just for demonstration purposes, so that the new data
    # animates in.
    time.sleep(0.1)
