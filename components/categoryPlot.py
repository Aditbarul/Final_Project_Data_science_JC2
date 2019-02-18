import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('diamonds.csv')

listGOFunc = {
    "bar": go.Bar,
    "violin": go.Violin,
    "box": go.Box
}

def getPlot(jenisPlot,jenisDiamond):
    return[listGOFunc[jenisPlot](
            x=df[jenisDiamond],
            y=df['price'],
            text=df['price'],                        
            opacity=0.7,
            name='Total'
        )]        
    
