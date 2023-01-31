from dash import html 
import dash_mantine_components as dmc

from app import app

layout = html.Div([
    dmc.Grid(grow=True, gutter='lg', children=[
        # dmc.Col(dmc.Paper(p='lg', shadow='md', withBorder=True, children=[
        #     html.Img(src=app.get_asset_url("graph.jpg"), style={'maxWidth': '100%'})
        # ]), span=12),
        dmc.Col(dmc.Grid(grow=True, gutter='sm', children=[
            dmc.Col(dmc.Paper(p='sm', shadow='md', withBorder=True, children=[
                    html.Img(src=app.get_asset_url("pict1.webp"), style={'maxWidth': '100%'})
                ]), span=12),
            dmc.Col(dmc.Paper(p='sm', shadow='md', withBorder=True, children=[
                dmc.Text('''
                    My name is Abhinav Reddy, and I am the founder of PoliSent. I’ve worked in politics
                    for a few years and have always sought to improve civic participation through voter 
                    registration drives, public policy proposals, phone banking, and canvassing. PoliSent
                    has been created with a similar intention, specifically to make it easier for all citizens
                    to see how opinion towards a variety of social issues changes based on the state.
                ''', size='md')
            ]), span=12)
        ]), span=7),
        dmc.Col(dmc.Paper(p='lg', shadow='md', withBorder=True, children=[
            html.Img(src=app.get_asset_url("pict2.webp"), style={'maxWidth': '100%'})
        ]), span=5)
    ])
], style={'margin': '10%'})