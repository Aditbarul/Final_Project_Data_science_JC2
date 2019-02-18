import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

color_set = ['#80aaff','#cc0000']


def renderScatterPlot(df) :
    return html.Div([
                html.H1('Scatter Plot Diamonds', className='h1'),
                dcc.Graph(
                    id='scatterPlot',
                    figure={
                        'data': [
                            go.Scatter(
                                x=df['carat'],
                                y=df['price'],
                                mode='markers',
                            )],
                        'layout': go.Layout(
                            xaxis= dict(title='Carat'),
                            yaxis={'title': 'Price'},
                            margin={ 'l': 40, 'b': 40, 't': 10, 'r': 10 },
                            hovermode='closest'
                        )
                    }
                )
            ])