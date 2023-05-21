import clickhouse_connect

class ClickHouseOperations:

    def __init__(self, host, username, password):
        self.client = clickhouse_connect.get_client(host=host, username=username, password=password)

    def create_table(self, table_name, fields, engine="MergeTree()", order_by=""):
        field_list = ', '.join([f'{k} {v}' for k, v in fields.items()])
        query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                {field_list}
            ) ENGINE = {engine} ORDER BY {order_by}
        '''
        self.client.command(query)

    def insert_data(self, table_name, data, column_names):
        self.client.insert(table_name, data, column_names=column_names)
