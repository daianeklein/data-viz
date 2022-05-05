import pandas as pd
import re
import os

from dash import Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import base64


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags = [{'name' : 'viewport',
                              'content' : 'width=dice_width, initial-scale=1.0'}])


app.layout = dbc.Container([
    html.P(' '),
    html.Div(id = '1st-line-separator', style = {'border' : '4px LightCoral solid'}),   
        dbc.Card([
            dbc.CardBody([
                html.H2('ACIDENTES RODOVIÁRIOS', style = {'color' : '#F8F9F9'},
                   className = 'text-center'),
                html.H5('2008 à 2021', style = {'color' : '#F8F9F9'},
                   className = 'text-center')
                    ],  style={'border' : 'none'})
                ]),     
    html.P(' '),
    html.Div([
        html.Span('Dashboard referente a acidentes rodoviários registrados no período de 2008 à 2021\ne disponibilizados pela Polícia Federal do Brasil'),
        ], style = {'color' : '#A6ACAF', 'fontSize': 10, 'font-weight': 'light'},
    className = 'text-center'),
    html.P(' '),    
    html.Div(id = '2st-line-separator', style = {'border' : '2px #343a40 solid'}),
    html.P(' '),
    
    html.Div([
    dbc.Row([
        dbc.Col([
            html.H1('Ano da ocorrência', style = {'color' : 'white', 'fontSize' : 9,
                                                    'font-weight' : 'light',
                                                  'font-weight' : 'light'
                                                    })
        ], width = {'size' : 5, 'offset' : 0}) ]),
    dbc.Row([
        dbc.Col([
            dcc.Slider(min = 2007, max = 2021, value = 2007, step = 1,
                       className = 'year-slider',
                      marks = {str(i) : i for i in df['year'].unique()})
        ], width = {'size' : '100%'})
    
        ], className = 'container-year-slider',
            style = {'backgroundColor' : '#282828',
                    'width' : '50%'}),
    dbc.Col([
        html.H1('UF da ocorrência', style = {'color' : 'white', 'fontSize' : 9,
                                            'font-weight' : 'light',
                                            'font-weight' : 'light'})
    ], width = {'size' : 4, 'offset' : 5})
        ])
    
])
        

if __name__ == '__main__':
    app.run_server()