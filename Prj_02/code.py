import numpy as np
import simplekml
import pprint
import requests
import pandas as pd

kml = simplekml.Kml()

headers = {'User-Agent':'Some user agent'}
data = requests.post('https://www.myshiptracking.com/requests/vesselsonmaptempTTT.php?type=json&minlat=-77.3891307952422&maxlat=77.38913079524195&minlon=-180.06165291234876&maxlon=180.06165291234876&zoom=1&selid=-1&seltype=0&timecode=-1&filters=%7B%22vtypes%22%3A%22%2C0%2C3%2C4%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%22%2C%22ports%22%3A%221%22%2C%22minsog%22%3A0%2C%22maxsog%22%3A60%2C%22minsz%22%3A0%2C%22maxsz%22%3A500%2C%22minyr%22%3A1950%2C%22maxyr%22%3A2024%2C%22status%22%3A%22%22%2C%22mapflt_from%22%3A%22%22%2C%22mapflt_dest%22%3A%22%22%7D',headers=headers).text

data = [x.split("\t")[:-1] for x in data.split("\n")][3:-2]

# Define column names for your DataFrame
columns = ['col1', 'col2', 'col3', 'name', 'lat', 'lon', 'col7', 'col8', 'col9', 'col10']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# print(df)
###ADDING A COLUMN "altitude" WITH RANDOM VALUES FROM 200 TO 2000
df['altitude']=df.groupby('name').name.transform(lambda x: 0)

###CALLING THE COLUMNS OF INTEREST
df=df[['lon', 'lat', 'altitude', 'name']]

df.apply(lambda X: kml.newpoint(name=X["name"], coords=[( X["lon"],X["lat"])]) ,axis=1)
kml.save(path = "data.kml")

# Import necessary modules
from qgis.core import QgsVectorLayer, QgsProject

# Define the file path of the KML file
file_path = "data.kml"

# Define layer name
layer_name = "Ships Layer"

# Load the KML file as a vector layer
layer = QgsVectorLayer(file_path, layer_name, "ogr")

# Check if the layer was loaded successfully
if not layer.isValid():
    print("Layer failed to load!")

# Add the layer to the map canvas
QgsProject.instance().addMapLayer(layer)

# Create a symbol
symbol = QgsSymbol.defaultSymbol(layer.geometryType())

# Define the symbol properties (e.g., color, size, etc.)
symbol.setColor(QColor(255, 0, 0))  # Red color
symbol.setSize(1.5)  # Symbol size

# Create a renderer
renderer = QgsSingleSymbolRenderer(symbol)

# Assign the renderer to the layer
layer.setRenderer(renderer)

# Refresh the layer to reflect the changes
layer.triggerRepaint()
