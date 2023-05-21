import json
import pandas as pd
from helpers.clickhouse_operations import ClickHouseOperations
from helpers import config

def load_data(zipcodes_datafile_geojson):
    with open(zipcodes_datafile_geojson) as file:
        data = json.load(file)

    rows = []
    for feature in data["features"]:
        row = {
            "zip": feature["properties"]["zip"],
            "type": feature["geometry"]["type"],
            "coordinates": str(feature["geometry"]["coordinates"])
        }
        rows.append(row)

    df = pd.DataFrame(rows)

    fields = {
        'zip': 'String',
        'type': 'String',
        'coordinates': 'String'
    }
    db = ClickHouseOperations(config.DB_HOST, config.DB_USERNAME, config.DB_PASSWORD)
    db.create_table(table_name='zip_codes', fields=fields, order_by='zip')

    # Prepare data for insertion
    data = [list(row) for row in df.itertuples(index=False, name=None)]

    db.insert_data('zip_codes', data, ['zip', 'type', 'coordinates'])


if __name__ == "__main__":
    zipcodes_datafile_geojson = '/home/dvieira/tmp/easyhealth/eh-analytics/src/2023-05-19_01.58.58-usa_zip_codes_v7.geo.json'
    load_data(zipcodes_datafile_geojson)
