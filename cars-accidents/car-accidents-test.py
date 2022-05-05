# -*- coding: utf-8 -*-

import pandas as pd
import re
import os

from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import base64

# #reading data
# path = 'data'
# lista = []
# df = pd.DataFrame()

# for f in os.listdir(path + "/"):
#     frames = pd.read_csv(path + "/" + f, encoding = 'latin-1', sep = ';', low_memory = False)
#     file = re.search(r'\d+', f).group(0)
    
#     frames['file'] = file
#     df = df.append(frames, ignore_index=True)

# df['data_inversa'] = df['data_inversa'].astype('datetime64')

# df['month'] = df['data_inversa'].dt.month
# df['year'] = df['data_inversa'].dt.year

# df['time'] = df['horario'].str.slice(0, 2)

# df1 = df[['dia_semana', 'uf', 'br', 'km',
#        'municipio', 'causa_acidente', 'tipo_acidente',
#         'fase_dia', 
#        'condicao_metereologica', 'tipo_pista', 
#        'pessoas', 'mortos', 'feridos_leves', 'feridos_graves', 'ilesos',
#        'ignorados', 'feridos', 'file', 'month', 'year', 'time']]

# #replacing some values
# df1 = df1.copy(deep = True)

# df1['dia_semana'] = [x.lower() for x in df1['dia_semana']]
# df1['dia_semana'] = [x.replace('-feira', '') for x in df1['dia_semana']]

# df1['causa_acidente'] = df1['causa_acidente'].str.lower()

# dict_replace = {'ingestão de álcool e/ou substâncias psicoativas pelo pedestre' : 'ingestão de álcool',
#                'ingestão de álcool ou de substâncias psicoativas pelo pedestre' : 'ingestão de álcool',
#                'ingestão de álcool pelo condutor' : 'ingestão de álcool',
#                'redutor de velocidade em desacordo' : 'velocidade incompatível',
#                'dormindo' : 'condutor dormindo',
#                'falta de atenção à condução' : 'falta de atenção',
#                'defeito mecânico em veículo' : 'defeito mecânico no veículo',
#                'mal súbito do condutor' : 'mal súbito'}

# df1 = df1.replace({'causa_acidente' : dict_replace})

# df1.to_csv('cars_accident_formated.csv', sep = ";", index = False)
####
df1 = pd.read_csv('cars_accident_formated.csv', sep = ';')

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags = [{'name' : 'viewport',
                              'content' : 'width=dice_width, initial-scale=1.0'}])


app.layout = dbc.Container([
    html.P(' '),
    html.Div(id = '1st-line-separator', style = {'border' : '4px LightCoral solid'}),   
        dbc.Card([
            dbc.CardBody([
                html.H1('ACIDENTES RODOVIÁRIOS', style = {'color' : '#F8F9F9'},
                   className = 'text-center'),
                html.H5('2008 à 2021', style = {'color' : '#F8F9F9'},
                   className = 'text-center')
                    ],  style={'border' : 'none'})
                ]),     
    html.P(' '),
    html.Div([
        html.Span('Dashboard referente a acidentes rodoviários registrados no períiodo de 2008 à 2021\ne disponibilizados pela Polícia Federal do Brasil'),
        ], style = {'color' : '#A6ACAF', 'fontSize': 14, 'font-weight': 'light'},
    className = 'text-center'),
    html.P(' '),    
    html.Div(id = '2st-line-separator', style = {'border' : '1px Lightpink solid'}),
    html.P(' '),
    
    dbc.Row([
        dbc.Col([
            html.H1('Ano da ocorrência', style = {'color' : '#A6ACAF', 'fontSize' : 10,
                                                    'font-weight' : 'light',
                                                    'backgroundColor' : 'orange'})
        ], width = {'size' : 2, 'offset' : 0}),
        dbc.Col([
            
            html.H1('Ano da da daocorrência', style = {'color' : '#A6ACAF', 'fontSize' : 10, 'font-weight' : 'light',
                                             'backgroundColor' : 'red'})
            ], width = {'size' : 2,'offset' : 3}),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Slider(id = 'year-slider', min = 2007, max = 2021, value = 2007, step = 1,
                      marks = {i: i for i in range(2007, 2021)}, color = 'lightcoral')
        ], width = {'size' : 6})
    ])
])

if __name__ == '__main__':
    app.run_server()


