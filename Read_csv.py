import folium
import pandas as pd
import numpy as np
from folium.features import ColorLine
from time import sleep
import branca.colormap as cm
# Refresh time
refresh_after = 3

# Create the map with Opentreetmap background
map = folium.Map(location=(48.075, 11.64), zoom_start=15, control_scale=True, prefer_canvas=True)

# Define constants
value_min = 1.5
value_max = 3
value_averange = (value_min + value_max)/2

# Show colormap
colormap = cm.LinearColormap(["green", "yellow", "red"], vmin=value_min, vmax=value_max)
colormap.add_to(map)
it = 0


for i in range(100):
    data = pd.read_csv("/home/hung/AnacondaProjects/Studentenarbeit/Position_with_intensity_of_wave.csv", sep="\t")
    data = np.array(data)
    if data.shape[0] < 2:
        pass
    # Wir müssen colorline so erstellen, dass Mittelpunkt jeder Line ist die gegebense Position
    # Annahme position: [1, 2, 3, 4, 5]
    # Wir machen 2 Liste: Array_1: [1, 2, 3, 4, 5, 5]
    #                     Array_2: [1, 1, 2, 3, 4, 5]
    # Position für Poliline: (Array_1 + Array_2)/2
    #                         [1, 1.5, 2.5, 3.5, 4.5, 5]
    lats = data[:, 0]
    lons = data[:, 1]
    intensity = data[:, 2]
    lats_a1 = np.append(lats, lats[-1])
    lats_a2 = np.append(lats[0], lats)
    new_lats = (lats_a1 + lats_a2) / 2
    new_lats = new_lats.reshape((data.shape[0] + 1, 1))
    lons_a1 = np.append(lons, lons[-1])
    lons_a2 = np.append(lons[0], lons)
    new_lons = (lons_a1 + lons_a2) / 2
    new_lons = new_lons.reshape((data.shape[0] + 1, 1))
    new_position = np.concatenate((new_lats, new_lons), axis=1)

    # Create color line
    colorline = ColorLine(positions=new_position, colors=intensity, colormap=colormap, weight=5)
    colorline.add_to(map)
    map.save("Test_Reload.html")
    sleep(refresh_after)
    it += 1
    print(it)