from dash import html, dcc, clientside_callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_mantine_components as dmc

from app import app
from pages import Home, About


server = app.server 

header = dmc.Header(
    height=80, 
    fixed=True,
    children=[
        dmc.Container(
            fluid=True,
            children=dmc.Group(
                position='apart', 
                children=[
                    dmc.Center(
                        dcc.Link(
                            dmc.Title("PoliSent", order=1, color='#FFFFFF'), 
                            href='/', 
                            style={"paddingTop": "10%", "textDecoration": "none"}
                        )
                    ),
                    dmc.Center(
                        dcc.Link(
                            dmc.Text('ABOUT', size='md', color='#FFFFFF'),   
                            style={"paddingTop": "40%", "textDecoration": "none"},
                            href='/about'
                        )
                    )
            ]), 
            style={'marginLeft': '1rem', 'marginRight': '1rem'}
        )
    ], style={"backgroundColor": "#000000"}, 
)

app.layout = html.Div([
    dcc.Location(id='url'),
    header,
    html.Div(id='page-content', style={'marginTop': '10rem'})
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_content(url): 
    if url == '/' or url == 'Home': 
        return Home.layout
    elif url == '/about': 
        return About.layout
    else: 
        return html.H1('Error 404!')


if __name__ == '__main__':
    app.run_server(debug=False)

