import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
import plotly.graph_objs as go

PAGE_SIZE = 10


def renderTable(df) :
    return html.Div([
        html.Table([      
        ],style={ 'width': '300px', 'paddingBottom': '20px' }),
        html.Div(id='divTable', children=[
            html.H1('Diamond Dataset', className='h1'),
            html.H4(['Total Row : ' + str(len(df))]),
            dcc.Graph(
                id='tableData',
                figure= {
                    'data': [
                        go.Table(
                            header=dict(
                                values=['<b>'+ col +'</b>' for col in df.columns],
                                font = dict(size = 14),
                                height = 30,
                                fill = dict(color='#a1c3d1')
                            ),
                            cells=dict(
                                values=[df[col] for col in df.columns],
                                font = dict(size = 12),
                                height = 30,
                                fill = dict(color='#EDFAFF'),
                                align = ['center']
                            )
                        )
                    ],
                    'layout': dict(height=500,margin={'l': 0, 'b': 40, 't': 10, 'r': 0})
                }
            )
        ])
    ])
