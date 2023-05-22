import clickhouse_connect
import logging
from helpers import db_access_config as config
import pandas as pd
from typing import Union

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

    def query_df(self, query: str) -> Union[pd.DataFrame, None]:
        """
        Execute a query on ClickHouse and return the result as a pandas DataFrame.

        Args:
            query (str): The query to execute.

        Returns:
            pandas.DataFrame or None: The query result as a DataFrame, or None if an error occurred.
        """
        return self.client.query_df(query)
