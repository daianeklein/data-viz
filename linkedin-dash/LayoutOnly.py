import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

data = 'https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Berlin_crimes.csv'
df = pd.read_csv(data)
df = df.groupby('District')[['Street_robbery', 'Drugs']].median()

app.layout = html.Div([
    dbc.Row(dbc.Col(html.H3("Our Beaultiful Layout"),
                    width ={'size' : 6, 'offset' : 3}
                    ),
            ),

    dbc.Row(dbc.Col(html.Div("One column is all we need because there ain't no room for the both of us in this raggedy town"),
                    width = {'size' : 4, 'offset' : 0} 
                    )
            ),

    dbc.Row(
        [
            dbc.Col(dcc.Dropdown(id='c_dropdown', placeholder = 'last dropdown',
                                options = [{'label' : 'Option A', 'value' : 'OptA'},
                                           {'label' : 'Option B', 'value' : 'OptB'}]),
                                width ={'size' : 4, 'offset' : 0, 'order' : 3}
                    ),

            dbc.Col(dcc.Dropdown(id = 'a_dropdown', placeholder = 'first dropdown',
                                options = [{'label' : 'Option A', 'value' : 'OptA'},
                                           {'label' : 'Option B', 'value' : 'OptB'}]),
                                width = {'size' : 4, 'offset' : 0, 'order' : 1}
                    ),

            dbc.Col(dcc.Dropdown(id = 'b_dropdown', placeholder = 'second dropdown',
                                options = [{'label' : 'Option A', 'value' : 'OptA'},
                                           {'label' : 'Option B', 'value' : 'OptB'}]),
                                width = {'size' : 4, 'offset': 0, 'order' : 2})
        ]
    )

])

if __name__ == "__main__":
    app.run_server()