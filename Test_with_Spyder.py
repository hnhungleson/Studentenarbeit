#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 23:25:09 2018

@author: hung
"""

import folium
import pandas as pd
from folium.plugins import TimestampedGeoJson, MeasureControl, Draw, Fullscreen
from numpy.random import random, seed
seed(0)


map = folium.Map(location=(48.13, 11.57), zoom_start=13, control_scale=True, 
                 prefer_canvas=True)

# Add fullscreen
fs = Fullscreen(position="topleft")
fs.add_to(map)

lat_init, lon_init = 48.13, 11.57 # München
for i in range(10):
    new_lat, new_lon = lat_init + i * 0.01, lon_init + i * 0.01
    point = folium.map.Marker(location=(new_lat, new_lon), popup='Latitude: {}\nLongitude: {}'.format(new_lat, new_lon))
    point.add_to(map)
    
lat_init, lon_init = 48.13, 11.58 # München
for i in range(10):
    point = folium.Circle(location=(lat_init + i * 0.01, lon_init + i * 0.01), popup='Point {}'.format(i),
                                  radius=50, fill=True, fill_color="b", fill_opacity=1.)
    point.add_to(map)
    
# Add tool to display line
data = {"dep": ["Place_MontpellierMediterranee_Airport", "Place_Bristol___Lulsgate"],
       "dest": ["Place_BastiaPoretta_Airport", "Place_TenerifeSur_ReinaSofia_Airport"],
       "geojson": [{"type": "LineString","coordinates": [[3.961389, 43.583333], [3.968056, 43.580833], [3.974722, 43.578333], [3.986389, 43.575278], [3.998333, 43.5725], [4.163333, 43.530556], [4.269167, 43.503889], [4.398889, 43.471111], [4.540278, 43.435278], [4.716944, 43.390556], [4.917222, 43.34], [4.928889, 43.336944], [5.159722, 43.276667], [5.333056, 43.231667], [5.729722, 43.229167], [5.828889, 43.228611], [6.023889, 43.226667], [6.601944, 43.219444], [6.841667, 43.346111], [6.893333, 43.373333], [7.3625, 43.327778], [7.621389, 43.301944], [8.303056, 43.170833], [8.434722, 43.145556], [8.626944, 43.118333], [8.759167, 43.099722], [9.059444, 43.057222], [9.083333, 43.053889], [9.395556, 42.978333], [9.488333, 42.955833], [9.603889, 42.927778], [9.574444, 42.847222], [9.568056, 42.829444], [9.542222, 42.758889], [9.526111, 42.714722], [9.513333, 42.679444], [9.506944, 42.661944], [9.474722, 42.573611], [9.484722, 42.55]]}, 
                  {"type": "LineString","coordinates": [[-2.719167, 51.382778], [-2.736111, 51.382778], [-2.787222, 51.382222], [-2.838333, 51.381944], [-2.866389, 51.366111], [-2.894722, 51.350278], [-2.998056, 51.2925], [-3.359722, 51.178611], [-3.362778, 51.161111], [-3.371944, 51.108889], [-3.384167, 51.039167], [-3.388611, 51.013056], [-3.398056, 50.957778], [-3.416944, 50.8475], [-3.423889, 50.809167], [-3.431944, 50.761667], [-3.448333, 50.666667], [-3.4525, 50.641389], [-3.463889, 50.574167], [-3.473333, 50.518611], [-3.493611, 50.398611], [-3.495556, 50.362778], [-3.505278, 50.184167], [-3.517222, 49.960556], [-3.529444, 49.737222], [-3.558333, 49.658611], [-3.638611, 49.44], [-3.728333, 49.195278], [-3.783056, 49.046944], [-3.808611, 48.976944], [-4.061667, 48.301944], [-4.184722, 47.957222], [-4.3125, 47.829444], [-4.524722, 47.591389], [-4.990556, 47.079167], [-5.408056, 46.612778], [-6.919722, 44.835278], [-7.012778, 44.698056], [-7.143889, 44.504444], [-8.926667, 41.872778], [-9.016111, 41.667778], [-9.161389, 41.334444], [-10.234444, 38.873333], [-11.448333, 35.966667], [-12.911667, 34.261111], [-13.836111, 33.149444], [-15.301667, 31.300833], [-15.850278, 30.433889], [-16.372778, 29.591389], [-16.990556, 28.928056], [-17.023056, 28.893333], [-17.094444, 28.816389], [-17.211667, 28.690833], [-17.263611, 28.635], [-17.315556, 28.579167], [-17.374167, 28.516389], [-17.439167, 28.446389], [-17.452222, 28.4325], [-17.375278, 28.389444], [-17.29, 28.341667], [-17.196111, 28.289167], [-17.170556, 28.274722], [-17.115, 28.234444], [-17.027778, 28.170833], [-16.877222, 28.061389], [-16.773056, 28.028889], [-16.687778, 28.0025], [-16.676389, 28.006667], [-16.647222, 28.017222], [-16.622222, 28.026389], [-16.604167, 28.033056], [-16.5725, 28.044444]]}]}
data_frame = pd.DataFrame(data=data)

def style_function(feature):
    return {
        'fillColor': '#ffaf00',
        'color': 'blue',
        'weight': 1.5,
        'dashArray': '5, 5'
    }


def highlight_function(feature):
    return {
        'fillColor': '#ffaf00',
        'color': 'green',
        'weight': 3,
        'dashArray': '5, 5'
    }


for index, row in data_frame.iterrows():
    c = folium.GeoJson(row["geojson"], name=("{}{}".format(row["dep"], row["dest"])),
                       overlay=True, style_function=style_function, highlight_function=highlight_function)
    folium.Popup("{}\n{}".format(row["dep"], row["dest"])).add_to(c)
    c.add_to(map)

    
folium.LayerControl(position="bottomright").add_to(map)

line = folium.PolyLine(locations=[(lat_init, lon_init), (lat_init + 0.1, lon_init+0.1)], color="blue", weight=2.5, opacity=1)
line.add_to(map)

# Create a polyline animation on map
# The number of points muss equal the number of times: len(coordinates) = len(time)
coordinates = []
time = []
time_stamp = 1435708800000
for i in range(100):
    lat = lat_init + i * 0.01 * random()
    lon = lon_init + (i+1) * 0.01 * random()
    coordinates.append([lon, lat])
    time.append(time_stamp + i * 60000)
print(coordinates)
print(time)

poly_line = TimestampedGeoJson(data={
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coordinates,
            },
            "properties": {
                "times": time,
                "style": {
                    "color": "red",
                    "weight": 2
                }
            }
        }
    ]
}, period="PT1M")

poly_line.add_to(map)

# Create a tool to measure distance and area
tool_measure = MeasureControl()
tool_measure.add_to(map)

# Create tool to draw something
tool_draw = Draw()
tool_draw.add_to(map)
map.save("Munich_with_points_and_lines_.html")
