import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

path = '/Users/daianeklein/Documents/DataScience/Data-Viz/Plotly-Dash/Plotly-Dash/Plotly-Dashboards-with-Dash/Data/mpg.csv'
df = pd.read_csv(path)

# Add a random "jitter" to model_year to spread out the plot
df['year'] = random.randint(-4,5,len(df))*0.10 + df['model_year']

app.layout = html.Div([
    html.Div([
            dcc.Graph(
        id='mpg_scatter',
        figure={
            'data': [go.Scatter(
                x = df['year']+1900,  # our "jittered" data
                y = df['mpg'],
                text = df['name'],
                hoverinfo = 'text',
                mode = 'markers'
            )],
            'layout': go.Layout(
                title = 'mpg.csv dataset',
                xaxis = {'title': 'model year'},
                yaxis = {'title': 'miles per gallon'},
                hovermode='closest'
            )
    ]),
        

        }
    )
])

if __name__ == '__main__':
    app.run_server()



