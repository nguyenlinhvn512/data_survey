import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
import matplotlib.patches as patches
import folium


df = pd.read_csv(
    "Police_Department_Incidents_-_Previous_Year__2016.csv")
df.drop(['IncidntNum', 'Category', 'Descript', 'DayOfWeek', 'Date', 'Time',
          'Resolution', 'Address', 'X', 'Y', 'Location', 'PdId'], axis=1, inplace=True)
# df1 = df['PdDistrict'].value_counts().to_frame(
#     name='Count')
#df1 = df['PdDistrict'].value_counts().to_frame(name='Count')
#df.reset_index()
#df1.rename(columns={'index': 'Neighbourhood'}, inplace=True)
print("")
df = df.value_counts().rename_axis('Neighbourhood').reset_index(name='Counts')
print(df.head(10))



sf_geo = r'san-francisco.geojson'  # geojson file

latitude = 37.77
longitude = -122.42

# create map and display it
sf_map = folium.Map(location=[latitude, longitude], zoom_start=12)

sf_map.choropleth(geo_data=sf_geo,
                               data=df,
                               columns=['Neighbourhood', 'Counts'],
                               # This is the parameter you left out and it specifies the column in the geojson file to be linked to the Neighborhood column in your dataframe
                               key_on='feature.properties.DISTRICT',
                               fill_color='YlOrRd',
                               fill_opacity=0.7,
                               line_opacity=0.2,
                               legend_name='Crime Rate in San Francisco')

sf_map.save("San_Francisco.html")
