import plotly.express as px
import pandas as pd
from dash import dcc, html

def get_abortion():
    states = pd.read_csv("./data/states.csv")
    AllCountryPop = pd.read_csv("./data/PoliSent Data.csv")
    AllCountryPop = AllCountryPop.merge(states, left_on='State', right_on='State', how='inner')
    AllCountryPop = AllCountryPop[['Code', 'Abortion']]
    AllCountryPop['hover'] = AllCountryPop['Code'] + '\n' + AllCountryPop['Abortion'].astype(str)

    graph_properties = dict(
        scope='usa',
        showland=True,
        landcolor='white',
        bgcolor='white'
    )

    font = dict(
        family='DM Sans',
        size=15,
        color='black'
    )

    label = dict(
        bgcolor='#EEEEEE',
        bordercolor='aquamarine',
        font=font
    )

    fig = px.choropleth(AllCountryPop, locations='Code', color='Abortion',
                        locationmode='USA-states', color_continuous_scale='Greys')

    fig.update_layout(
        geo=graph_properties, 
        font=dict(family='DM Sans'), 
        margin=dict(t=0,r=0,b=0,l=0),
        height= 600
    )
    fig.update_traces(text=AllCountryPop['hover'], hoverinfo='text')
    fig.update_layout(coloraxis_colorbar=dict(title='Abortion'))
    fig.update_layout(hoverlabel=label)
    # fig.update_layout(displayModeBar=False)

    return html.Div(dcc.Graph(figure=fig), style={'marginBottom': '3rem'})


def get_existence_of_climate_change(): 
    states = pd.read_csv("./data/states.csv")
    AllCountryPop = pd.read_csv("./data/PoliSent Data.csv")
    AllCountryPop = AllCountryPop.merge(states, left_on='State', right_on='State')
    AllCountryPop = AllCountryPop[['Code', 'Existence_of_Climate_Change']]
    AllCountryPop['hover'] = AllCountryPop['Code'] + "\n" + AllCountryPop['Existence_of_Climate_Change'].astype(str)
    graph_properties = dict(
        scope='usa',
        showland=True,
        landcolor='white',
        bgcolor='white'
    )

    font = dict(
        family='DM Sans',
        size=15,
        color='black'
    )

    label = dict(
        bgcolor='#EEEEEE',
        bordercolor='aquamarine',
        font=font
    )
    fig = px.choropleth(
                AllCountryPop,
                locations='Code',
                color='Existence_of_Climate_Change',
                color_continuous_scale='Greys',
                # title='Question: Should Climate Change be Taught in Schools?',
                # hover_data=['hover'],
                locationmode='USA-states',
                scope='usa',
                template='plotly_white'
    )
    fig.update_layout(
        geo=graph_properties, 
        font=dict(family='DM Sans'), 
        margin=dict(t=0,r=0,b=0,l=0),
        height= 600
    )
    fig.update_traces(text=AllCountryPop['hover'], hoverinfo='text')
    fig.update_layout(coloraxis_colorbar=dict(title='Existence of Climate Change'))
    fig.update_layout(hoverlabel=label)

    map = html.Div([
        dcc.Graph(
            figure=fig,
        )
    ], style={'marginBottom': '3rem'})

    return map


def get_gov_aid_to_the_poor(): 
    df_states = pd.read_csv('states.csv')
    df_aid = pd.read_csv('PoliSent Data.csv', dtype={'Government_Aid_to_the_Poor': float})
    df_aid = df_aid.merge(df_states, left_on='State', right_on='State')
    df_aid = df_aid[['Code', 'Government_Aid_to_the_Poor']]
    df_aid['hover'] = df_aid['Code'] + '<br>' + df_aid['Government_Aid_to_the_Poor'].astype(str)

    fig = px.choropleth(df_aid, 
                        locations='Code', 
                        color='Government_Aid_to_the_Poor', 
                        color_continuous_scale='Greys', 
                        locationmode='USA-states',
                        # title='Question: Should Government Aid to the Poor be Supported?',
                        # hover_data=['hover'],
                        #hoverinfo='text'
                        )

    fig.update_layout(geo=dict(
        scope='usa',
        showland=True,
        landcolor='white',
        bgcolor='white'
    ))

    fig.update_layout(hoverlabel=dict(
        bgcolor='#EEEEEE',
        bordercolor='aliceblue',
        font=dict(
            family='DM Sans',
            size=15,
            color='black'
        )
    ))

    fig.update_layout(
        coloraxis_colorbar=dict(title='Government Aid to the Poor', tickfont=dict(family='DM Sans')),
        title_font=dict(
            family='DM Sans', 
        ), 
        margin=dict(t=0,r=0,b=0,l=0),
        height= 600
    )

    fig.update_traces(text=df_aid['hover'], hoverinfo='text')
    map = html.Div([
        dcc.Graph(
            figure=fig,
        )
    ], style={'marginBottom': '3rem'})

    return map

def get_same_sex_mariage(): 
    states = pd.read_csv("./data/states.csv")
    AllCountryPop = pd.read_csv("./data/PoliSent Data.csv")
    AllCountryPop = AllCountryPop.merge(states, left_on='State', right_on='State')
    AllCountryPop = AllCountryPop[['Code', 'Same_Sex_Marriage']]
    AllCountryPop['hover'] = AllCountryPop['Code'].astype(str) + "\n" + AllCountryPop['Same_Sex_Marriage'].astype(str)

    fig = px.choropleth(AllCountryPop, locations='Code', color='Same_Sex_Marriage', color_continuous_scale='Greys',
                        locationmode='USA-states'
    )

    fig.update_layout(
        geo=dict(scope='usa', showland=True, landcolor='white', bgcolor='white'), 
        # colorbar=dict(), 
        coloraxis_colorbar=dict(
            title='Same Sex Marriage', 
            tickfont=dict(family='DM Sans')
        ),
        hoverlabel=dict(
            bgcolor='#EEEEEE', 
            bordercolor='aliceblue', 
            font=dict(
                family="DM Sans", 
                size=15, 
                color="black"
            )
        ),
        showlegend=False, 
        # displayModeBar=False, 
        margin=dict(t=0, r=0, b=0, l=0),
        height= 600
    )
    fig.update_traces(text=AllCountryPop['hover'], hoverinfo='text')

    map = html.Div([
        dcc.Graph(
            figure=fig,
        )
    ], style={'marginBottom': '3rem'})

    return map


def get_protecting_the_env(): 
    states = pd.read_csv("./data/states.csv")
    AllCountryPop = pd.read_csv("./data/PoliSent Data.csv")
    AllCountryPop = AllCountryPop.merge(states, left_on='State', right_on='State')
    AllCountryPop = AllCountryPop[['Code', 'Protecting_the_Environment']]
    AllCountryPop['hover'] = AllCountryPop['Code'].astype(str) + "\n" + AllCountryPop['Protecting_the_Environment'].astype(str)

    fig = px.choropleth(
        AllCountryPop, 
        locations='Code', 
        color='Protecting_the_Environment', 
        color_continuous_scale="Greys", 
        locationmode='USA-states'
    )

    fig.update_layout(
        geo = dict(showland=True, landcolor='white', bgcolor='white', scope='usa'),
        title_font=dict(family="DM Sans"), 
        font=dict(family="DM Sans"), 
        hoverlabel=dict(bgcolor='#EEEEEE', 
            bordercolor='aliceblue', 
            font=dict(family='DM Sans', size=15, color='black')
        ), 
        margin=dict(t=0,r=0,b=0,l=0),
        height= 600
    )

    fig.update_layout(coloraxis_colorbar=dict(title='Protecting the Env', tickfont=dict(family='DM Sans')))
    map = html.Div([
        dcc.Graph(
            figure=fig,
        )
    ], style={'marginBottom': '3rem'})
    return map


def get_human_evolution(): 
    states = pd.read_csv("./data/states.csv")
    AllCountryPop = pd.read_csv("./data/PoliSent Data.csv")
    AllCountryPop = AllCountryPop.merge(states, left_on="State", right_on="State")
    AllCountryPop = AllCountryPop[["Code", "Human_Evolution"]].assign(hover=AllCountryPop["Code"] + "\n" + AllCountryPop["Human_Evolution"].astype(str))

    font = dict(
        family="DM Sans",
        size=15,
        color="black"
    )

    label = dict(
        bgcolor="#EEEEEE",
        bordercolor="aliceblue",
        font=font
    )

    fig = px.choropleth(
        AllCountryPop,
        locations="Code",
        color="Human_Evolution",
        color_continuous_scale="Greys",
        locationmode='USA-states',
        labels=label,
    )

    fig.update_layout(
        geo = dict(showland=True, landcolor='white', bgcolor='white', scope='usa'),
        coloraxis_colorbar=dict(title='Human Evolution', tickfont=dict(family='DM Sans')), 
        margin=dict(t=0,r=0,b=0,l=0),
        height= 600
    )
    map = html.Div([
        dcc.Graph(
            figure=fig,
        )
    ], style={'marginBottom': '3rem'})
    return map


def get_immigration_reform(): 
    states = pd.read_csv("./data/states.csv")
    AllCountryPop = pd.read_csv("./data/PoliSent Data.csv")
    AllCountryPop = AllCountryPop.merge(states, left_on='State', right_on='State', how='inner')
    AllCountryPop = AllCountryPop[['Code', 'Immigration_Reform']]
    AllCountryPop['hover'] = AllCountryPop['Code'] + "\n" + AllCountryPop['Immigration_Reform'].astype(str)

    font = dict(
        family = "DM Sans",
        size = 15,
        color = "black"
    )

    label = dict(
        bgcolor = "#EEEEEE",
        bordercolor = "aliceblue",
        font = font
    )

    fig = px.choropleth(
        AllCountryPop,
        locations = 'Code',
        color = 'Immigration_Reform',
        color_continuous_scale = "Greys",
        locationmode = 'USA-states'
    )

    fig.update_layout(
        geo = dict(showland=True, landcolor='white', bgcolor='white', scope='usa'),
        coloraxis_colorbar=dict(title='Immigration Reform', titlefont=font), 
        hoverlabel=label, 
        margin=dict(t=0,r=0,b=0,l=0),
        height= 600

    )
    fig.update_traces(marker=dict(line=dict(width=0.5, color='gray')))

    map = html.Div([
        dcc.Graph(
            figure=fig
        )
    ], style={'marginBottom': '3rem'})
    return map



