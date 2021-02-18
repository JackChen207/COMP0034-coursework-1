import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

%matplotlib inline

# Read the data for the population (F001) into a data frame skipping the second heading row
population_data = pd.read_csv('parliamentary-constituency-profiles-data.csv', usecols=["POPULATION"], skiprows=[1])
