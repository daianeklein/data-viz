import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

markdown_text = '''
### Dash and Markdown
Dash app can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org) specification of Markdown.
Check out thir [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div([

            html.Label('Markdown'),
            dcc.Markdown(children=markdown_text),

             html.Label('Dropdown'),
             dcc.Dropdown(options = [{'label' : 'New York City',
                                        'value' : 'NYC'},
                                        
                                     {'label' : 'San Francisco',
                                        'value' : 'SF'}],
                                        
                            value = 'SF'), #default value

            html.P(html.Label('Radio Itens - Test')),
            dcc.RadioItems(
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montréal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'),

            html.P(html.Label('Slider')),
            dcc.Slider(min = -10, max = 10, step= 0.5, value = 0, #value = default value
            marks = {i: i for i in range(-10, 10)}), #add markers

            html.Label('Some Radio Items'),
            dcc.RadioItems(
                options = [
                    {'label' : 'New York City', 'value' : 'NYC'},
                    {'label' : 'San Francisco', 'value' : 'SF'}
                    ],                         
                value = 'SF' #pre selected value
), 

# add not overlapping html - Radio Items

            html.P(html.Label('Some Radio Items')), 
            dcc.RadioItems(
                options=[
                    {'label' : 'Los Angeles', 'value' : 'LA'},
                    {'label' : 'Arizona',     'value' : 'AZ'}
            ],              
                            value='AZ')
            

])

if __name__ == '__main__':
    app.run_server()