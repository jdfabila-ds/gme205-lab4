import os
import json
import shapely
from shapely.geometry import Polygon

from spatial import Parcel


PARCEL_DATA_PATH = "data/parcels_shapely_ready.json"
GRID_DATA_PATH = "data/suitability_grid.json"
OUTPUT_DIR = "output"

with open( PARCEL_DATA_PATH, "r", encoding="utf-8") as file:
    data = json.load(file)

# ---  Creating the parcel list from the json file

parcels = []
for record in data:
    parcel_obj = Parcel.from_dict(record)
    parcels.append(parcel_obj)

#print( type(parcels))
#print ( parcels[1].is_active)


#--- Q: What is the total area of active parcels?
totalarea_sqm = 0
for p in parcels:
    if (p.is_active == True):
        totalarea_sqm += p.area_sqm

print(f"Total area of active parcels: {totalarea_sqm:.2f} square meters" )
        


