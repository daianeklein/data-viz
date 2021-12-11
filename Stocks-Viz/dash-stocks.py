import pandas as pd
import pandas_datareader.data as web

import datetime

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

import plotly.express as px


#start = datetime.datetime(2020,1, 1)
#end = datetime.datetime(2020, 12, 3)
#df = web.DataReader(['AMZN','GOOGL','FB','PFE','MRNA','BNTX'],
#                    'stooq', start=start, end=end)

#df = df.stack().reset_index()
#df.to_csv('stocks-data.csv', index = False)

df = pd.read_csv('stocks-data.csv')
print(df[:15])

# https://www.bootstrapcdn.com/bootswatch/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

app.layout = dbc.Container([
            dbc.Row([
                dbc.Col(html.H1('Stock Market Dashboard',  
                                className = 'text-center text-primary, mb-4'), #text-primery = color | mb-4 == padding
                                width = 12)                                                                                  
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(id = 'my-dropdown', multi = False, value = 'AMZN', #multi = multiple values selected
                    options = [{'label': x, 'value': x } for x in sorted(df['Symbols'].unique())]),

                dcc.Graph(id='line-fig', figure={})
                ], #width ={'size' : 5, 'offset' : 1, 'order' : 1},
                           xs = 12, sm = 12, md = 12, lg = 5, xl = 5),

                dbc.Col([
                    dcc.Dropdown(id='my-dropdown2', multi = True, value = ['PFE', 'BNTX'],
                                options = [{'label' : x, 'value' : x} for x in sorted(df['Symbols'].unique())], 
                                ), 
                    dcc.Graph(id = 'line-fig2', figure = {})
                ], #width = {'size' : 5, 'offset' : 1, 'order' : 2},
                            xs = 12, sm = 12, md = 12, lg = 5, xl = 5)
            ], justify = 'start'), #, justify='start'

            dbc.Row([
        dbc.Col([
            html.P("Select Company Stock:",
                   style={"textDecoration": "underline"}),
            dcc.Checklist(id='my-checklist', value=['FB', 'GOOGL', 'AMZN'],
                          options=[{'label':x, 'value':x}
                                   for x in sorted(df['Symbols'].unique())],
                          labelClassName='text-primary m-2'),
            dcc.Graph(id = 'my-hist', figure = {})
                ], #width = {'size' : 5, 'offset' : 0}
                            xs = 12, sm = 12, md = 12, lg = 5, xl = 5),

            dbc.Col([
                dbc.Card([
                    dbc.CardBody(
                        html.P("We're better together. Help each other out!",
                                className = 'card-text')
                    ),
                    dbc.CardImg(
                        src = "https://media.giphy.com/media/Ll0jnPa6IS8eI/giphy.gif",
                        bottom = True),
                ],
                    style = {'width' : '24rem'},
                )],
                    xs = 12, sm = 12, md = 12, lg = 5, xl = 5)
            ], align = 'center')
            ], fluid = True) # ,fluid = True | right and left space

@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dropdown', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols']==stock_slctd]
    figln = px.line(dff, x='Date', y='High')
    return figln


# Line chart - multiple
@app.callback(
    Output('line-fig2', 'figure'),
    Input('my-dropdown2', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    figln2 = px.line(dff, x='Date', y='Open', color='Symbols')
    return figln2

# Histogram
@app.callback(
    Output('my-hist', 'figure'),
    Input('my-checklist', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    dff = dff[dff['Date']=='2020-12-03']
    fighist = px.histogram(dff, x='Symbols', y='Close')
    return fighist


if __name__ == '__main__':
    app.run_server()

help(dash.dcc.Checklist)