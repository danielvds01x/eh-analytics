import clickhouse_connect
import logging
from helpers import db_access_config as config

class ClickHouseOperations:
    def __init__(self, host=None, username=None, password=None):
        self.client = clickhouse_connect.get_client(host=config.DB_HOST, username=config.DB_USERNAME, password=config.DB_PASSWORD)

    def create_table(self, table_name, fields, engine="MergeTree()", order_by=""):
        field_list = ', '.join([f'{k} {v}' for k, v in fields.items()])
        query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                {field_list}
            ) ENGINE = {engine} ORDER BY {order_by}
        '''
        self.client.command(query)

    def drop_table_if_exists(self, table_name):
        self.client.command(f'DROP TABLE IF EXISTS {table_name}')

    # def insert_data(self, table_name, data, column_names):
    #     self.client.insert(table_name, data, column_names)

    def insert_data(self, table_name, data, column_names='*'):
        self.client.insert(table_name, data, column_names=column_names)

    def insert_df(self, table_name, df):
        self.client.insert_df(table_name, df)

    def check_if_table_exists(self, table_name):
        try:
            result = self.client.command(f"SHOW TABLES LIKE '{table_name}'")
            return len(result) > 0
        except Exception as e:
            logging.error(f"An error occurred when checking if the table exists: {e}")
            return False
