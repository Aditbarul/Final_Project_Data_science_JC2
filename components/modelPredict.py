import pandas as pd
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv('diamonds.csv')
cut_indicators = ['Fair', 'Good', 'Very Good','Premium', 'Ideal'] #df['cut'].unique()
color_indicators = ['D', 'E', 'F', 'G','H', 'I', 'J']#df['color'].unique()
clarity_indicators = ['I1', 'SI1', 'SI2', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']#df['clarity'].unique()

def renderModelPredict() :
    return html.Div([
                html.H1('Test Predict Diamonds', className='h1'),
                html.Div(children=[
                    html.Div([
                        html.P('Carat : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputCaratPredict', type='number', value='0')
                    ],className='col-4'),
                    
                    html.Div([
                        html.P('Cut : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputCutPredict',
                        options=[{'label': i, 'value': i} for i in cut_indicators],
                        value='Fair')
                    ],className='col-4'),

                    html.Div([
                        html.P('Color : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputColorPredict',
                        options=[{'label': i, 'value': i} for i in color_indicators],
                        value='D')
                    ],className='col-4'),

                    html.Div([
                        html.P('Clarity : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(id='inputClarityPredict',
                        options=[{'label': i, 'value': i} for i in clarity_indicators],
                        value='I1')
                    ],className='col-4'),

                    html.Div([
                        html.P('Depth : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputDepthPredict', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('table : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputTablePredict', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('x : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputXPredict', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('y : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputYPredict', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.P('z : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputZPredict', type='number', value='0')
                    ],className='col-4'),

                    html.Div([
                        html.Button('Predict', id='buttonPredict', className='btn btn-primary')
                    ],className='mx-auto', style={ 'paddingTop': '20px', 'paddingBottom': '20px' })
                ],className='row'),
                html.Div([
                    html.H2('', id='outputPredict', className='mx-auto')
                ], className='row')
            ])