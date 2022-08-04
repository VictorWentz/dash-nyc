from _components import (
        _controllers,
        _histogram,
        _map
)

import plotly.express as px

import numpy as np


def generate_df_inter(df, location, square_size):
    if location is None:
        df_inter = df.copy()
        return df_inter
    else:
        df_inter = df[df['BOROUGH'] == location] if location != 0 else df.copy()
        size_limit = _controllers.slider_size[square_size] if square_size is not None else \
            df['GROSS SQUARE FEET'].max()
        df_inter = df_inter[df_inter['GROSS SQUARE FEET'] <= size_limit]
        return df_inter

def get_color_map(df, variable_color):
    
    colors_rgb = px.colors.sequential.GnBu

    df_quantiles = df[variable_color].quantile(np.linspace(0,1, len(colors_rgb))).to_frame()

    df_quantiles = (df_quantiles - df_quantiles.min()) / (df_quantiles.max() - df_quantiles.min())

    df_quantiles['colors'] = colors_rgb

    df_quantiles.set_index(variable_color, inplace=True)

    colors_scale = [[i,j] for i, j in df_quantiles['colors'].iteritems()]

    return colors_scale