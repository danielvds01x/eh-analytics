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
from table_irs_soi_stats import config

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )


def load_data(file_path):
    logging.info('Loading data from CSV file.')

    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
    else:
        print("File does not exist or is not a regular file")
        sys.exit(1)

    # Rename the columns using the field_mapping dictionary
    df.rename(columns={k: v['readable_name'] for k, v in config.FIELD_MAPPING.items()}, inplace=True)

    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Convert columns to String
    columns_to_convert = ['state_fips_code', 'state', 'zip_code']
    df[columns_to_convert] = df[columns_to_convert].astype(str)

    logging.info('Dataframe created.')

    table_name = 'irs_soi_stats_2020_noagi'
    fields = {v['readable_name']: v['data_type'] for v in config.FIELD_MAPPING.values()}

    logging.info('Setting up ClickHouse operations.')
    db = ClickHouseOperations()

    # Prepare data for insertion
    logging.info('Preparing data for insertion.')
    logging.info('Inserting data.')
    db.drop_table_if_exists(table_name)
    db.create_table(table_name=table_name, fields=fields, order_by='zip_code')
    db.insert_df(table_name, df)
    logging.info('Data inserted successfully.')

if __name__ == "__main__":
    setup_logging()

    irs_soi_stats_data_file = os.path.join(ROOT_DIR, '_input/irs', '2023-05-19_14.11.58-20zpallnoagi.csv')
    print(irs_soi_stats_data_file)

    load_data(irs_soi_stats_data_file)
