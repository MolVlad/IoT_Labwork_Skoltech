import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_core_components as dcc

app_path = str(pathlib.Path(__file__).parent.resolve())

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}

data = pd.read_csv(os.path.join(app_path, os.path.join("data", "data.csv")))

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Sales by categories statistics', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'Food', 'value':'Food'},
            {'label': 'Hobbies', 'value':'Hobbies'},
            {'label': 'Household', 'value':'Household'},
            ],
        value = 'Food'),
        dcc.Graph(id = 'bar_plot')
    ])

@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x = data['index'], y = data['{}'.format(dropdown_value)],\
                     line = dict(color = 'firebrick', width = 4))
                     ])
    
    fig.update_layout(title = 'Sales in Wallmart by categories',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Sales, k'
                      )
    return fig  


