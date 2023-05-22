import json
import pandas as pd
import logging
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
parent_dir = os.path.dirname(current_dir)  # Get the parent directory
sys.path.insert(0, parent_dir)  # Add the parent directory to the beginning of the system path

from config.definitions import ROOT_DIR
from helpers.clickhouse_operations import ClickHouseOperations

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def load_data(zipcodes_datafile_geojson):
    logging.info('Loading data from JSON file.')
    with open(zipcodes_datafile_geojson) as file:
        data = json.load(file)

    rows = []
    logging.info('Parsing features from JSON data.')
    for feature in data["features"]:
        row = {
            "zip": feature["properties"]["zip"],
            "type": feature["geometry"]["type"],
            "coordinates": str(feature["geometry"]["coordinates"])
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    logging.info('Dataframe created.')

    table_name = 'zip_codes'

    fields = {
        'zip': 'String',
        'type': 'String',
        'coordinates': 'String'
    }

    logging.info('Setting up ClickHouse operations.')
    db = ClickHouseOperations()

    # Prepare data for insertion
    logging.info('Preparing data for insertion.')
    data = [list(row) for row in df.itertuples(index=False, name=None)]

    logging.info('Inserting data.')
    db.drop_table_if_exists(table_name)
    db.create_table(table_name=table_name, fields=fields, order_by='zip')
    db.insert_data(table_name=table_name, data=data, column_names=fields.keys())
    logging.info('Data inserted successfully.')

if __name__ == "__main__":
    setup_logging()

    zipcodes_datafile_geojson = os.path.join(ROOT_DIR, '_input', '2023-05-19_01.58.58-usa_zip_codes_v7.geo.json')
    print(zipcodes_datafile_geojson)

    load_data(zipcodes_datafile_geojson)