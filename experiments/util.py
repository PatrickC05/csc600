import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point

def polsby_popper(row):
    return row['geometry'].area / ((row['geometry'].length / 2 / np.pi )**2 * np.pi)

def reock(row):
    # bounds = row['geometry'].envelope.bounds
    e = row['geometry'].envelope
    x = e.bounds[2]
    y= e.bounds[3]
    t = Point(x, y)
    return row['geometry'].area / (np.pi* e.centroid.distance(t)**2)


path = "./data/shapefiles/Interim Congressional.shp"
df = gpd.read_file(path)
df['reock'] = df.apply(reock, axis=1)