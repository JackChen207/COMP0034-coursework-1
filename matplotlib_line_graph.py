import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

%matplotlib inline

# Read the data for the population and crime into a data frame skipping the second heading row
data = pd.read_csv('parliamentary-constituency-profiles-data.csv', usecols=["Crime Rate", "F010"], skiprows=[1])

# Create a new DataFrame with the required Date column
population = data.loc[:,['F010']]
crime = data.loc[:,['Crime Rate']]

fig, axes = plt.subplots(figsize=(12, 6))

plt.plot(population, crime, 'o')
axes.set_xlabel('Population Density')
axes.set_ylabel('Crime Rate')
axes.set_title('The graph of Population Density against Crime Rate')
