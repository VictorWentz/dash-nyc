import dash_bootstrap_components as dbc
from dash import html



contatoVictor = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="assets\eu.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Victor Hugo Wentz", className="card-title"),
                            html.P(
                                'Data Scientist',
                                className="card-text",
                            ),
                            html.Small([
                                dbc.CardLink("Linkedin", href="https://www.linkedin.com/in/victor-wentz/")
                            ],
                                
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px", 'margin-top': '50px'},
)

contatoVini = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="assets\\vini.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Vinicios Henrique Wentz", className="card-title"),
                            html.P(
                                'Senior Software Engineer',
                                className="card-text",
                            ),
                            html.Small([
                                dbc.CardLink("Linkedin", href="https://www.linkedin.com/in/vinicios-wentz-b507828a/")
                            ],
                                
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px"},
)


# contato = dbc.Card([
#     dbc.Row(
#         dbc.Col(
#             dbc.CardImg(
#                 src = 'assets\eu.png',
#                 className = "img-fluid rounded-start",
#             ),
#             className='col-md-4'
#         ),
#         dbc.Col(
#             dbc.CardBody([
#                 html.H4('Victor Hugo Wentz'),
#                 html.P('Cientista de Dados'),
#                 html.Small('Contato: '),
#                 dbc.CardLink("Linkdin", href="https://www.linkedin.com/in/victor-wentz/"),
#             ]
#             ),
#             className='col-md-8')
#     ),
#     dbc.Row(
#         dbc.CardBody([
#             html.H4('Vinicios Henrique Wentz'),
#             html.P('Senior Software Engineer'),
#             html.Small('Contato: '),
#             dbc.CardLink("Linkdin", href="https://www.linkedin.com/in/vinicios-wentz-b507828a/"),
#         ]
#         )
#     )
# ]
    
# )