import plotly.express as px
import pandas as pd
import json


# Read the data for the population into a data frame skipping the second heading row
population_data = pd.read_csv('parliamentary-constituency-profiles-data.csv', usecols=["GEO_CODE", "GEO_LABEL", "POPULATION"], skiprows=[1])
# Reduce the data London
london=['A11', 'A20', 'A22', 'A24', 'A26', 'A29', 'A62', 'A63', 'A64', 'A75', 'A86', 'A92', 'B01', 'B06', 'B08', 'B11', 'B26', 'B27', 'B28', 'B29', 'B45', 'B46', 'B47', 'B48', 'B51', 'B59', 'B62', 'B63', 'B64', 'B68', 'B73', 'B75', 'B90', 'B92', 'B93', 'B98', 'B99', 'C04', 'C05', 'C10', 'C14', 'C23', 'C24', 'C25', 'C32', 'C33', 'C36', 'C37', 'C41', 'C43', 'C60', 'C61', 'C62', 'C63', 'C96', 'D43', 'D46', 'D56', 'D61', 'D70', 'D74', 'D80', 'E53', 'E59', 'E73', 'E77', 'E80', 'E82', 'E83', 'E88', 'F08', 'F12', 'F16']
population_data = population_data[population_data['GEO_CODE'].isin(london)]

# Get the json data
with open('constituency.json') as json_file:
    geojson = json.load(json_file)

# Create the choropleth mapbox
fig = px.choropleth_mapbox(population_data,
                           geojson=geojson,
                           locations="GEO_CODE",
                           featureidkey="properties.PCON13CDO",
                           color="POPULATION",
                           color_continuous_scale='reds',
                           range_color=(80000, 140000),
                           mapbox_style="carto-positron",
                           zoom=8.5,
                           center = {"lat": 51.492658396880055, "lon": -0.07496962702302},
                           opacity=0.5,
                           hover_name="GEO_LABEL",
                           labels={'GEO_LABEL':'AREA'},
                           title="London population in the 2008 Census"
                          )

fig.show()
