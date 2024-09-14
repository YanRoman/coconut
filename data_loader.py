import sys

import pandas as pd
from loguru import logger
from sklearn.model_selection import train_test_split

DATA_MAX_SIZE = 20000


def create_df(file_path):
    try:
        df = pd.read_csv(f"{file_path}")
        logger.info(f"Файл {file_path} успешно загружен")

        if len(df) > DATA_MAX_SIZE:
            df = df.sample(n=DATA_MAX_SIZE, random_state=1)
            logger.info(f"Файл обрезан до {DATA_MAX_SIZE} записей.")
        return df

    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        sys.exit(1)


def extract_transactions(df):
    transactions = df.groupby('user_session')['product_id'].apply(list).reset_index()
    transactions.columns = ['user_session', 'product_ids']
    transactions = transactions[transactions['product_ids'].apply(len) > 1]
    return transactions


def split_train_test(df):
    test_df, train_df = train_test_split(df, test_size=0.2, random_state=42)
    return test_df, train_df
