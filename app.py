import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pickle
from components.diamondsTable import renderTable
# from components.scatterPlot import renderScatterPlot
from components.categoryPlot import  df, getPlot
from components.modelPredict import renderModelPredict

loadModel = pickle.load(open('pipe_diamonds.sav', 'rb'))

app = dash.Dash(__name__)

server = app.server

df = pd.read_csv('diamonds.csv')

app.title = 'Dashboard Diamonds'



app.layout = html.Div(children=[
    html.H1(children='Dashboard Diamonds',className='titleDashboard'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Diabetes Dataset', value='tab-1',children=[
            renderTable(df)
        ]),
        dcc.Tab(label='Scatter Plot', value='tab-2',children=[
            html.Div([
                html.H1('Scatter Plot Diamond', className='h1'),
                html.Div(children=[
                    html.Div([
                        dcc.Dropdown(
                            id='jenisDiamonds',
                            options=[{'label': i.capitalize(), 'value': i} for i in ['carat','x','y','z']],
                            value='carat',     
                        )
                    ],className='col-6'),
                ],className='row'),
                dcc.Graph(
                    id='scatterPlot',
                )
            ])
        ]),
        dcc.Tab(label='Category Plot', value='tab-3',children=[
            html.Div([
                html.H1('Categorical Plot Diamond', className='h1'),
                html.Div(children=[
                    html.Div([
                        dcc.Dropdown(
                            id='jenisPlot',
                            options=[{'label': i.capitalize(), 'value': i} for i in ['bar','box','violin']],
                            value='box',
                            
                        )
                    ],className='col-6'),
                    html.Div([
                        dcc.Dropdown(
                            id='jenisDiamond',
                            options=[{'label': i.capitalize(), 'value': i} for i in ['cut','color','clarity']],
                            value='cut',
                            
                        )
                     ],className='col-6'),
                ],className='row'),
                dcc.Graph(
                    id='categoricalPlot',
                )
            ])
        ]),
        dcc.Tab(label='Test Predict', value='tab-4',children=[
            renderModelPredict()
        ]),
    ], style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    })
], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})


@app.callback(
    Output(component_id='categoricalPlot', component_property='figure'),
    [Input(component_id='jenisPlot', component_property='value'),
    Input(component_id='jenisDiamond', component_property='value')]
)
def update_graph_categorical(jenisPlot,jenisDiamond):
    return {
        'data': getPlot(jenisPlot,jenisDiamond),
        'layout': go.Layout(
                    xaxis={'title':jenisDiamond},
                    yaxis={'title':'price'},
                    margin={'l':40,'b':40,'t':10,'r':10},
                    # legend={'x':0, 'y':1},
                    hovermode='closest',boxmode='group',violinmode='group'
                )
    }
 
@app.callback(
    Output(component_id='scatterPlot', component_property='figure'),
    [Input(component_id='jenisDiamonds', component_property='value')])

def update_graph_categorical(jenisDiamonds):
    return {
        'data':[go.Scatter(
            x=df[jenisDiamonds],
            y=df['price'],
            mode='markers',
        )],
        'layout': go.Layout(
            xaxis= dict(title=jenisDiamonds),
            yaxis={'title': 'Price'},
            margin={ 'l': 40, 'b': 40, 't': 10, 'r': 10 },
            hovermode='closest'
                    
                )
    }

@app.callback(
    Output('outputPredict', 'children'),
    [Input('buttonPredict', 'n_clicks')],
    [State('inputCaratPredict', 'value'), 
    State('inputCutPredict', 'value'),
    State('inputColorPredict', 'value'),
    State('inputClarityPredict', 'value'),
    State('inputDepthPredict', 'value'),
    State('inputTablePredict', 'value'),
    State('inputXPredict', 'value'),
    State('inputYPredict', 'value'),
    State('inputZPredict', 'value')])
def update_output(n_clicks, carat, cut, color, clarity, depth, table, x, y, z):
    data = [[carat,cut,color,clarity,depth,table,x,y,z]]
    prediction = loadModel.predict(data)
    return 'Prediction : ' + str(prediction)
    

if __name__ == '__main__':
    app.run_server(debug=True,port=1995)