# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/Pokemon.csv')

app.layout = html.Div(children=[
    html.H1(children='Exercise #2'),
    html.Div(children='''
        A scatter plot that visualizes the relationship between Pokemon attack and defense effort values.
    '''),

    dcc.Graph(
        id='pokemon-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['Attack'],
                    y=df['Defense'],
                    mode='markers',
                    text=df['Name'],
                    marker={
                        'size': 10,
                        'opacity': 0.8
                    }
                )
            ],
            'layout': {
                'title': 'Pokemon Attack vs. Defense Effort Values',
                'xaxis': {'title': 'Attack'},
                'yaxis': {'title': 'Defense'},
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
