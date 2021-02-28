import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# Read the data
data = pd.read_csv('parliamentary-constituency-profiles-data.csv', skiprows=[1])

# Create the bubble graph
fig = px.scatter(data,
                 x="POPULATION",
                 y="Crime Rate",
                 size="pop",
                 color="continent",
                 hover_name="GEO_LABEL",
                 log_x = True,
                 size_max=60,
                 )

fig.update_layout(
    title='Crime Rate v.s. Population',
    xaxis=dict(
        title='Population',
    ),
    yaxis=dict(
        title='Crime Rate',
    ),
)

app = dash.Dash(_name_)

# Create the app layout
app.layout = html.Div(children=[
    html.H1(children='Visualization of Population in Greater London'),

    html.Div(children='''
        A scatter plot of population in Greater London
    '''),

    dcc.Graph(
        id='example-graph',
        figure= fig,
        style={'width': '200vh', 'height': '90vh'}

    )
])

if _name_ == '_main_':
    app.run_server(debug=True)
