from dash import dcc
import dash_bootstrap_components as dbc


from dash import html, dcc
from app import app

list_of_locations = {
    'All': 0,
    'Manhattan': 1,
    'Bronx': 2,
    'Brooklyn': 3,
    'Queens': 4,
    'Staten Island': 5
}

variable_control = ['YEAR BUILT', 'TOTAL UNITS', 'SALE PRICE']

slider_size = [100, 500, 1000, 10000, 1000000]

controlers = dbc.Row([

    html.H1('Data Brothers'),
    # html.Img(id='logo', src = app.get_asset_url('logo_dark.png'), style={'width': '50%'}),
    html.H3('Vendas de imóveis - NYC', style={'margin-top': '30px'}),
    html.P('Utilize este dashbord para analisar vendas ocorridas na \
    cidade de New York no período de 1 ano.'),

    html.H4( 'Distrito', style = {'margin-top': '50px', 'margin-bottom': '25px'}),
    dcc.Dropdown(
        id = 'location-dropdown',
        options = [{'label': i, 'value': j} for i, j in list_of_locations.items()],
        value = 0,
        placeholder = 'Selecione um distrito'

    ),
    html.H4( 'Metragem (m²)', style = {'margin-top': '50px', 'margin-bottom': '25px'}),
    dcc.Slider(
        min = 0,
        max = 4,
        id = 'meters-slider',
        marks = {i: str(j) for i,j in enumerate(slider_size)},
        value = 0

    ),
    html.H4( 'Variável de controle', style = {'margin-top': '50px', 'margin-bottom': '25px'}),

    dcc.Dropdown(
        id = 'variable-control-dropdown',
        options = [{'label': i, 'value': i} for i in variable_control],
        value = 'SALE PRICE',
        placeholder = 'Selecione uma varável'

    )

])
