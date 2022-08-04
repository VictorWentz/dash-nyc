from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from dataset.data_process import DataSystemProcess

from _components import (
        _controllers,
        _histogram,
        _map,
        _contact
)

from utils import *

from app import app

# Data ingestion
dataSystem = DataSystemProcess('dataset\cleaned_data.csv')

df = dataSystem.get_clean_data()



# Layout
app.layout = dbc.Container(
        children=[
                dbc.Row([
                        dbc.Col([_controllers.controlers, _contact.contatoVictor,
                        _contact.contatoVini ], md=3),
                        dbc.Col([_map.map, _histogram.hist], md=9),
                ])

        ], fluid=True, )


# Callbacks
@app.callback(
        Output('histogram-graph','figure'),
        [
                Input('location-dropdown','value'),
                Input('meters-slider','value'),
                Input('variable-control-dropdown','value')
        ]
)
def update_histogram(location, square_size, color_map):
        
        df_inter = generate_df_inter(df, location, square_size)

        hist_fig = px.histogram(df_inter, x = color_map, opacity=0.75)

        hist_layout = go.Layout(
                margin = go.layout.Margin(l=10,r=0,t=0,b=50),
                showlegend=False,
                template='plotly_dark',
                paper_bgcolor='rgba(0, 0, 0, 0)'
        )

        hist_fig.layout = hist_layout

        return hist_fig
        

@app.callback(
        Output('map-graph','figure'),
        [
                Input('location-dropdown','value'),
                Input('meters-slider','value'),
                Input('variable-control-dropdown','value')
        ]
)
def update_map(location, square_size, color_map):
        
        df_inter = generate_df_inter(df, location, square_size)

        lat, lon = dataSystem.means_lat_long()

        colors_scale = get_color_map(df_inter, color_map)

        px.set_mapbox_access_token(open('keys\mapbox_key').read())

        map_fig = px.scatter_mapbox(df_inter, lat = 'LATITUDE', lon = 'LONGITUDE', 
        color=color_map, size='size_m2', size_max=15, zoom=10, opacity=0.4)

        map_fig.update_layout(mapbox=dict(center=go.layout.mapbox.Center(lat=lat,lon=lon)),
        margin=go.layout.Margin(l=10,r=10,t=10,b=10))

        map_fig.update_coloraxes(colorscale=colors_scale)

        return map_fig



if __name__ == '__main__':
    app.run_server(debug=True)