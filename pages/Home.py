from dash import html, dcc
from dash.dependencies import Input, Output
import dash_mantine_components as dmc

from components import Graphs
from app import app


layout = html.Div(
    dmc.Grid(grow=True, gutter="xl", children=[
        dmc.Col(dcc.Loading(html.Div(id='map')), span=12),
        dmc.Col(dmc.Center(
            dmc.Select(
                id='select_map_dataset',
                label="What are American's Views on...", 
                data=[
                    'Abortion', 
                    'Government Aid to the Poor', 
                    'Same-Sex Marriage', 
                    'Protecting the Environment', 
                    'Human Evolution', 
                    'Existence of Climate Change', 
                    'Immigration Reform'
                ], 
                value='Abortion', 
                style={'minWidth': '300px'}
            )
        ), span=12)
    ])
)


@app.callback(
    Output('map', 'children'),
    Input('select_map_dataset', 'value'), 
)
def update_map(data):
    if data == 'Abortion': 
        return Graphs.get_abortion()
    elif data == 'Existence of Climate Change': 
        return Graphs.get_existence_of_climate_change()
    elif data == 'Government Aid to the Poor': 
        return Graphs.get_gov_aid_to_the_poor()
    elif data == 'Same-Sex Marriage': 
        return Graphs.get_same_sex_mariage()
    elif data == 'Protecting the Environment': 
        return Graphs.get_protecting_the_env()
    elif data == 'Human Evolution': 
        return Graphs.get_human_evolution()
    elif data == 'Immigration Reform': 
        return Graphs.get_immigration_reform()

    else: 
        return 'Graph is not available yet!'


