import pandas as pd

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from plotly.offline import plot, iplot
import plotly.graph_objs as go

import numpy as np
import plotly.plotly as py

import plotly.plotly as py
from plotly.graph_objs import *



dataFrame = pd.read_excel("C:/Users/eduar/Desktop/data.xlsx")


dataTableRows = dataFrame.to_dict('records')
x_values=['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
y_values = [ '382,240', '510,286','558,442','586,755','729,260', '832,746','963,035', '1,081,984','1,203,745', 
            '1,192,119','1,259,657 ',' 1,494,779']
data=[go.Scatter(x=x_values, y=y_values, line=dict(width=0.5, color='rgb(255, 102, 217)'),
    fill='tonexty')]
layout=dict(title="<b>Arrivals by Years</b>")
figure_1 = dict(data=data, layout=layout)
arrival = dcc.Graph(id="arrival", figure=figure_1)

#Chart Departures
x_values_2=['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
y_values_2 = [ ' 337,064', '467,573','515,548','551,682','715,470', '830,492','965,372', ' 1,080,021','1,198,060', 
            '1,187,369','1,262,687 ',' 1,481,755']
data_2=[go.Scatter(x=x_values_2, y=y_values_2, line=dict(width=0.5, color='rgb(131, 90, 241)'),
    fill='tonexty')]
layout_2=dict(title="<b>Departures by Years</b>")
figure_2 = dict(data=data_2, layout=layout_2)
departure = dcc.Graph(id="departure", figure=figure_2)




countries = ['Russia','Georgia','Iran','USA','Ukraine','Philippines','France','Germany','Poland','India','Great Britain','UAE','China','Syria','Japan','Other']
country_colors = ['rgb(135, 135, 125)', 'rgb(210, 50, 0)', 'rgb(50, 90, 255)',
                 'rgb(178, 0, 0)', 'rgb(235, 235, 210)', 'rgb(235, 205, 130)',
                 'rgb(55, 255, 217)', 'rgb(38, 0, 171)', 'rgb(255, 255, 255)',
                 'rgb(244, 66, 188)','rgb(244, 65, 68)','rgb(136, 237, 239)',
                 'rgb(62, 109, 55)','rgb(135, 63, 39)','rgb(232, 210, 18)',
                 'rgb(48, 239, 19)','rgb(152, 196, 145)']
distance_from_arm = [4633, 286, 1149, 10540, 1439, 7963, 3495, 2922, 2374,3871,3640,2026,5108,791,7755,3866]
prc_change = [28.9, 11.9, 16.6, 39.7, 20.4, 159.4, 16.4, 27.0, 40.2,181.6, 30.0, 165.9, 75.7,4.4, 18.3,-10.9]
visitors_in2017 = [584561,319902,220147,44587,29706,22007,21881,21011,13378,11585,9005,8299,5747,3089,3026,176848]
visitors_in2016 = [453572,285762,188851,31941,24668,8484,18791,16541,9544,4114,6927,3121,3270,2958,2558,198555]

# Create trace, sizing bubbles by arrivals in 2017
trace1 = Scatter3d(
    x = distance_from_arm,
    y = prc_change,
    z = visitors_in2017,
    text = countries,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 3500, 
        size = visitors_in2017,
        color = country_colors,
        )  
)
data=[trace1]

layout=Layout(width=1500, height=800, title = 'Countries!',
              scene = dict(xaxis=dict(title='Distance from Armenia km',
                                      titlefont=dict(color='rgb(220, 220, 220)')),
                            yaxis=dict(title='Percentage Change',
                                       titlefont=dict(color='rgb(220, 220, 220)')),
                            zaxis=dict(title='Visitors in 2017',
                                       titlefont=dict(color='rgb(220, 220, 220)')),
                            bgcolor = 'rgb(20, 24, 54)'
                           )
             )

fig=dict(data=data, layout=layout)




app = dash.Dash()


app.layout = html.Div([

    html.Div([html.Div([html.H1("Armenian Tourism Overview", style={"color":"maroon", "text-align":"center", "font-family":"cursive"})], className="twelve columns")], className="row"),
    
    html.H3("Number of Visitors (2016-2017)",style={'color':'red',"textAlign":'left', 'fontFamily':"cursive"}),
    dt.DataTable(
        rows=dataTableRows,
        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id='datatable'
    ),


    html.Div([html.H3(children='Country Comparison by Distance', style={'color':'blue',"textAlign":'left', 'fontFamily':"cursive"}),
    dcc.Graph(id="myfigure",figure=fig),
    ]),

    html.Div([
        html.Div([
        html.Div([html.H3("Tourism Circulation", style={"color":"orange", "text-align":"left", "font-family":"cursive"})], className="twelve columns")], className="row"),
            html.Div([
            dcc.RadioItems(
            id = 'radiobutton',
            options=[
                {'label': 'Arrivals', 'value': 1},
                {'label': 'Departures', 'value': 2}
                ],
            ),
        ], className='three columns'),
       
        html.Div([], id = "Graph",className='nine columns')
    ],
    className='row')
], className='row')


@app.callback(
    Output(component_id="Graph", component_property='children'),
    [Input(component_id='radiobutton', component_property='value')],
    )
def update_graph(input_value):
    if input_value==1:
        return arrival
    elif input_value==2:
        return departure

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})



if __name__ == '__main__':
    app.run_server(debug=True)

