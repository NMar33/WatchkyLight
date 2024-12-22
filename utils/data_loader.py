# import pandas as pd
# from clickhouse_driver import Client
# import streamlit as st

# # Подключение к ClickHouse
# client = Client(host='localhost')

# @st.cache_data
# def load_data():
#     """
#     Загрузка данных из ClickHouse.

#     Возвращает:
#         pd.DataFrame: Данные из таблицы monitoring.logs.
#     """
#     query = """
#     SELECT * FROM monitoring.logs
#     """
#     data = client.execute(query, with_column_types=True)
#     df = pd.DataFrame(data[0], columns=[col[0] for col in data[1]])
    
#     # Преобразование timestamp в datetime
#     if 'timestamp' in df.columns:
#         df['timestamp'] = pd.to_datetime(df['timestamp'])
    
#     return df

import pandas as pd
from clickhouse_driver import Client
import streamlit as st
import json

SOURCE = 'local'
LOCAL_PATH = 'data/raw/logs.json'

if SOURCE == 'clickhouse':
# Подключение к ClickHouse
    client = Client(host='localhost')

@st.cache_data
def load_data(source=SOURCE, local_path=LOCAL_PATH):
    """
    Загрузка данных из ClickHouse или локального файла JSON.

    Аргументы:
        source (str): Источник данных ('clickhouse' или 'local').
        local_path (str): Путь к локальному файлу JSON.

    Возвращает:
        pd.DataFrame: Загруженные данные.
    """
    if source == 'clickhouse':
        query = """
        SELECT * FROM monitoring.logs
        """
        data = client.execute(query, with_column_types=True)
        df = pd.DataFrame(data[0], columns=[col[0] for col in data[1]])
    elif source == 'local':
        with open(local_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
    else:
        raise ValueError("source должен быть 'clickhouse' или 'local'")
    
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    return df
