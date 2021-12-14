import pandas as pd
import pandas_datareader.data as web

import datetime

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

import plotly.express as px


start = datetime.datetime(2020,1, 1)
end = datetime.datetime(2020, 12, 3)
#df = web.DataReader(['JNJ','SNY','NVS','PFE','MRNA','BNTX', 'AZN',
#                     'ABT', 'ABBV', 'BNTX'],
#                    'stooq', start=start, end=end)

#df = df.stack().reset_index()
#df.to_csv('stocks-data.csv', index = False)

#df = pd.read_csv('stocks-data.csv')
#print(df[:15])


df = pd.read_csv('/Users/daianeklein/Documents/DataScience/Data-Viz/Plotly-Dash/Plotly-Dash/data-viz/stocks-data.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}] )

app.layout = dbc.Container([
    html.P(' '),
    dbc.Row([
        dbc.Col(
            html.H1('STOCK MARKET DASHBOARD',
                    className = 'text-center text-primary, mb-4'))
    ]),

        html.Div(id='line-separator', style = {'border' : '2px white solid'}),
        html.P(' '),

    dbc.Row([
        dbc.Col(
            html.H6('Select Company Stock',
                    className = 'text left text-primary, mb-4'))
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Checklist(id='stock-checklist', value = [df['Symbols'].unique()],
                          options = [{'label' : x, 'value' : x} for x in df['Symbols'].unique()],
                          style = { 'display' : 'block'},
                          labelClassName = 'text-center m-2'),
                

            dbc.Checklist(id='stock-checklist2', value = [df['Symbols'].unique()],
                        options = [{'label' : x, 'value' : x} for x in df['Symbols'].unique()],
                       style = { 'display' : 'block'},
                       labelClassName = 'text-center m-2'),],
                        xs = 12, sm = 12, md = 12, lg = 3, xl = 3),
            
        dbc.Col([
            dcc.Graph(id='my-line-plot', figure = {},
            style = {'border' : '1px Azure Solid'})
        ], xs = 12, sm = 12, md = 12, lg = 9, xl = 9),

        
        ])
    

    ])

@app.callback(
    Output('my-line-plot', 'figure'),
    Input('stock-checklist', 'value')
)
def update_line_plot(stock_selected):
    df01 = df[df['Symbols'].isin(stock_selected)]
    figln = px.line(df01, x ='Date', y = 'High', color = 'Symbols')
    figln.update_layout({
        'plot_bgcolor' : 'rgba(0,0,0,0)',
        'paper_bgcolor' : 'rgba(0,0,0,0)'},
        title = {'text' : 'Stock Historical Prices',
                'y':0.9,
                'x':0.5,
                'xanchor' : 'center',
                'yanchor' : 'top'},
        legend_title = 'Stock Company',
        legend_title_font_color = 'yellow',
        font = dict(color = 'white'),
        xaxis_title = 'DATE',
        yaxis_title = 'DAY HIGH'
        )
    figln.update_xaxes(tickfont=dict(color = 'white'),
                        showgrid=False)

    figln.update_yaxes(showgrid=False)
    return figln



if __name__ == '__main__':
    app.run_server()
