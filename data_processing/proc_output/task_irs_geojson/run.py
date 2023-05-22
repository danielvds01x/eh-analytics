import pandas as pd
import json
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
parent_dir = os.path.dirname(os.path.dirname(current_dir))  # Get the parent directory
sys.path.insert(0, parent_dir)  # Add the parent directory to the beginning of the system path

from config.definitions import ROOT_DIR
from helpers.clickhouse_operations import ClickHouseOperations


# read in the input CSV file to a Pandas DataFrame
# df = pd.read_csv('input_data.csv')

db = ClickHouseOperations()

query = """
    SELECT
        zc.`type`,
        zc.coordinates,
        irs.zip_code,
        irs.total_medical_and_dental_expense_deduction_amount
    FROM
        irs_soi_stats_2020_noagi irs
        INNER JOIN zip_codes zc 
            ON irs.zip_code = zc.zip
"""

df = db.query_df(query)

# create a new empty list to store the GeoJSON features
features = []

# loop through each row in the DataFrame
for index, row in df.iterrows():
    # get the type and coordinates columns
    geom_type = row['type']
    coordinates = json.loads(row['coordinates'])
    
    # create a new dictionary for the feature
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': geom_type,
            'coordinates': coordinates
        },
        'properties': {
            'zip_code': row['zip_code'],
            'total_medical_and_dental_expense_deduction_amount': row['total_medical_and_dental_expense_deduction_amount']
        }
    }
    
    # add the feature to the list
    features.append(feature)

# create the final GeoJSON dictionary with the features list
geojson_dict = {
    'type': 'FeatureCollection',
    'features': features
}

# output the GeoJSON to a file
file = os.path.join(ROOT_DIR, 'src_output', 'output_geojson.json')
with open(file, 'w') as f:
    json.dump(geojson_dict, f)